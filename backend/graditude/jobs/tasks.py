import logging
from datetime import date, timedelta
from typing import Any, Dict, List, Union

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

from config import celery_app
from graditude.jobs.models import Company, Position, Post

# Get an instance of a logger
logger = logging.getLogger(__name__)


@celery_app.task()
def scrape_indeed(pages: List[int] = None):
    """
    Performs the web scrapping process using BeautifulSoup4 and pandas
    for data processing. The web page is fetched using the request
    library. Each job posting on the page are stored as
    'containers' with a class of 'row'. After fetching each container,
    perform parsing the fields of a post.
    """
    scraper = IndeedScraper(pages=pages)
    scraper.scrape()
    scraper.save_posts()


def parse_date(date_posted: str, today: date) -> Union[date, None]:
    """Parses the date field based to return the correct value.

    If the value is 'Just Posted' or 'Today', set day = 0.
    """
    if not date_posted:
        return None

    if date_posted in {"Just posted", "Today"}:
        days_ago = 0
    else:
        days_ago = int(date_posted[0]) if date_posted else 0

    return today - timedelta(days=days_ago)


def find_span(container: bs, tag: str, class_: str) -> Union[str, None]:
    """Searches a specified tag in a job post container.

    If the tag is found, return the stripped version of the text.
    Otherwise return None.
    """

    found = container.find(tag, class_=class_)
    if found is None:
        return None
    return found.text.strip()


class IndeedScraper:
    """A class representing an Indeed scraper."""

    # Base url to perform queries against
    url = "https://www.indeed.com/jobs?q="

    def __init__(self, pages=None):
        # The search queries to be used in requests
        positions = list(Position.objects.all())  # type: List[Position]
        self.search_queries = [obj.search_str() for obj in positions]  # type: List[str]

        # Every page contains 10 posts, so itereate in counts of 10
        self.pages = pages if pages else range(0, 1001, 10)

        # Stores the posts
        self.fields = [f.name for f in Post._meta.get_fields()]  # type: List[str]
        self.df = pd.DataFrame(columns=self.fields)  # type: pd.DataFrame

    def scrape(self):
        logger.info("Executing scraper")

        for query in self.search_queries:
            for page in self.pages:
                page_html = requests.get(
                    f"{self.url}{query}&sort=date&l=California&explvl=entry_level&sort=date&start={page}"
                )
                soup = bs(page_html.content, "html.parser")
                post_container = soup.findAll("div", {"class": "row"})
                self.parse_container(post_container)

        self.parse_posts()

    def parse_container(self, containers: List[bs]):
        """
        Parses the containers for the specified fields
        TODO: Make ID not equal to 1 for the source
        """
        today = date.today()
        span_fields = {"company", "location", "date"}

        for container in containers:
            post_href = container.find("a", {"class": "jobtitle"})["href"]

            fields = {
                f: find_span(container, "span", f) for f in span_fields
            }  # type: Dict[str, Any]

            fields.update(
                {
                    "date_posted": parse_date(fields["date"], today),
                    "title": container.a.text,
                    "date_added_db": today,
                    "description": find_span(container, "div", class_="summary"),
                    "source": 1,
                    "link": f"https://indeed.com/{post_href}",
                }
            )
            fields["is_sponsored"] = bool(fields["date_posted"])

            self.df = self.df.append(fields, ignore_index=True)

    def parse_posts(self):
        """Parses the dataframe containing all of the job posts.

        The first step is to remove companies that are spam, which is
        mainly 'Indeed Prime'. Afterwards, duplicate entries are dropped
        based on the 'company', 'date_posted', and 'title' fields. Often
        times there are multiple of the same job posting listed on
        different days which is not useful to search through for the end-user.
        """
        logger.info("Parsing posts")

        self.df.title = self.df.title.str.strip()

        spam_companies = ["Indeed Prime"]
        self.df = self.df[~self.df["company"].isin(spam_companies)]
        self.df = self.df.dropna(subset=["company"])
        self.df = self.df.drop_duplicates(subset=["company", "date_posted", "title"])

    def save_posts(self):
        """Saves each dataframe row as a record using get_or_create()."""
        logger.info("Savings posts to database")
        records = self.df.to_dict("records")

        for record in records:
            Company.objects.get_or_create(name=record["company"])

            Post.objects.get_or_create(
                title=record["title"],
                company_id=record["company"],
                defaults={
                    "date_posted": record["date_posted"],
                    "description": record["description"],
                    "location": record["location"],
                    "is_sponsored": False,
                    "date_added_db": record["date_added_db"],
                    "source_id": record["source"],
                    "link": record["link"],
                },
            )
