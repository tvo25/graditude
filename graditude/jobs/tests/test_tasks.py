from datetime import date

import requests
import pandas as pd
import pytest
from bs4 import BeautifulSoup as bs
from celery.result import EagerResult

from graditude.jobs.models import Company, Post
from graditude.jobs.tasks import IndeedScraper, parse_date, scrape_indeed
from graditude.jobs.tests.factories import PositionFactory, SourceFactory


@pytest.mark.django_db
def test_scrape_indeed(settings):
    """A basic test to execute the scrape_indeed Celery task."""
    settings.CELERY_TASK_ALWAYS_EAGER = True
    # Create the position
    PositionFactory(title="Software Engineer")
    SourceFactory(name="LinkedIn")

    # Check successful task invoke
    pages = list(range(0, 101, 10))
    task_result = scrape_indeed.delay(pages)
    assert isinstance(task_result, EagerResult)

    # Check that post objects exist
    assert Post.objects.exists()


def test_parse_date():
    """
    A test that executes the parse_date function, which should parse
    the string representation of a day (e.g. '3 days ago'), then
    subtracts from today (assuming 9/19/2019). The final result should
    be 9/16/2019 in date format.

    """
    date_posted = "3 days ago"
    today = date(2019, 9, 19)

    parsed_date = parse_date(date_posted, today)
    print(parsed_date)
    assert parsed_date == date(2019, 9, 16)


@pytest.mark.django_db
class TestIndeedScraper:
    """ A set of tests that executes the class methods of IndeedScraper """

    def test_scrape(self):
        """
        Test the scrape method using an integration test which runs
        all of the methods from the IndeedScraper class.
        """
        # Create the position
        PositionFactory(title="Software Engineer")
        SourceFactory(id=1, name="LinkedIn")

        # Check successful task invoke
        pages = list(range(0, 101, 10))

        scraper = IndeedScraper(pages)
        scraper.scrape()
        scraper.save_posts()
        assert Post.objects.exists()

    def test_parse_container(self):
        """
        Test the parse_container method to that the dataframe
        contains jobs posts from the url.
        """
        query = PositionFactory(title="Software Engineer").search_str()
        SourceFactory(id=1, name="LinkedIn")

        pages = list(range(0, 101, 10))
        scraper = IndeedScraper(pages)

        for page in scraper.pages:
            page_html = requests.get(
                f"https://www.indeed.com/jobs?q={query}&sort=date&l=California&explvl=entry_level&sort=date&start={page}"
            )
            soup = bs(page_html.content, "html.parser")
            post_container = soup.findAll("div", {"class": "row"})
            scraper.parse_container(post_container)

        assert not scraper.df.empty

    def test_parse_posts(self):
        """
        Test that the parse_posts method parses the dataframe of posts
        as specified.
        """
        scraper = IndeedScraper()
        today = date.today()

        source = SourceFactory()

        posts = [
            {
                "title": "Software Engineer",
                "company": "Graditude",
                "description": "Looking for Python expert",
                "location": "San Jose, CA",
                "is_sponsored": False,
                "date_posted": today,
                "date_added_db": today,
                "source": source.id,
                "link": "graditude.herokuapp.com",
                "position": "Full-time",
            },
            {
                "title": "Back End Engineer",
                "company": "Indeed Prime",
                "description": "Write some REST APIs in Django!",
                "location": "San Franciso, CA",
                "is_sponsored": False,
                "date_posted": today,
                "date_added_db": today,
                "source": source.id,
                "link": "graditude.herokuapp.com",
                "position": "Full-time",
            },
            {
                "title": "Front End Engineer",
                "company": None,
                "description": "You love QA?",
                "location": "Santa Clara, CA",
                "is_sponsored": False,
                "date_posted": today,
                "date_added_db": today,
                "source": source.id,
                "link": "graditude.herokuapp.com",
                "position": "Full-time",
            },
        ]
        for index, post in enumerate(posts):
            scraper.df = scraper.df.append(post, ignore_index=True)

        scraper.parse_posts()

        # Check no spam companies
        assert not ((scraper.df["company"]) == "Indeed Prime").any()

        # Check no null companies
        assert not scraper.df["company"].isnull().values.any()

        # Check no duplicates
        duplicates_exist = scraper.df.duplicated(
            subset=["company", "date_posted", "title"]
        )[0]
        assert not duplicates_exist

    def test_save_posts(self):
        """
        Tests the save_posts method saves the dataframe of parsed posts
        to the Post model with the necessary fields.
        """
        scraper = IndeedScraper()
        today = date.today()

        source = SourceFactory()
        post = {
            "title": "Software Engineer",
            "company": "Graditude",
            "description": "Looking for Python expert",
            "location": "San Jose, CA",
            "is_sponsored": False,
            "date_posted": today,
            "date_added_db": today,
            "source": source.id,
            "link": "graditude.herokuapp.com",
            "position": "Full-time",
        }

        scraper.df = scraper.df.append(post, ignore_index=True)

        scraper.save_posts()

        posts_exists = Post.objects.exists()
        companies_exist = Company.objects.exists()
        assert companies_exist and posts_exists
