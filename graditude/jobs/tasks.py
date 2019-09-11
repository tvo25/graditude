from datetime import date, timedelta
import requests
from typing import List, Union

import pandas as pd
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
from celery import shared_task

from graditude.jobs.models import Company, Position, Post

@shared_task(bind=True, task_name="Scrape Indeed")
def scrape_indeed(self):
    """
    Performs the web scrapping process using BeautifulSoup4 and pandas
    for data processing. The web page is fetched using the request
    library. Each job posting on the page are stored as
    'containers' with a class of 'row'. After fetching each container,
    perform parsing the fields of a post.
    """
    positions = Position.objects.all()
    searches = [obj.search_str() for obj in positions]

    pages = range(0, 1001, 10)

    fields = [f.name for f in Post._meta.get_fields()]
    df = pd.DataFrame(columns=fields)

    for search in searches:
        for page in tqdm(pages):
            page_html = requests.get(
                f"https://www.indeed.com/jobs?q={search}&sort=date&l=California&explvl=entry_level&sort=date&start={page}"
            )

            soup = bs(page_html.content, "html.parser")
            post_container = soup.findAll("div", {"class": "row"})

            df = parse_container(post_container, df)

    df = parse_postings(df)

    return df


def parse_container(containers: List[str], df: pd.DataFrame) -> pd.DataFrame:
    """ Parses the containers for the specified fields """
    today = date.today()

    span_fields = {'company', 'location', 'date'}

    for container in containers:
        post_href = container.find('a', {'class': 'jobtitle'})['href']

        fields = {f: find_span(container, 'span', f) for f in span_fields}
        fields.update({'date_posted': parse_date(fields['date'], today),
                       'title': container.a.text,
                       'date_added_db': today,
                       'description': find_span(container, "div", class_='summary'),
                       'source': 1,
                       'link': f'https://indeed.com/{post_href}'})
        fields['is_sponsored'] = True if fields["date_posted"] else False,

        df = df.append(fields, ignore_index=True)

    return df


def parse_date(date_posted, today):
    """
    Parses the date field based to return the correct value.
    if the value is 'Just Posted' or 'Today', set day = 0.
    """
    if not date_posted:
        return None

    if date_posted in {'Just posted', 'Today'}:
        days_ago = 0
    else:
        days_ago = int(date_posted[0]) if date_posted else 0

    return today - timedelta(days=days_ago)


def find_span(container: str, tag: str, class_: str) -> Union[str, None]:
    """
    Receives the job post container, and searches the tag for the
    specified value.
    If found, return the text.strip(), else return None.
    """
    found = container.find(tag, class_=class_)
    if found is None:
        return None
    return found.text.strip()


def parse_postings(df: pd.DataFrame) -> pd.DataFrame:
    """
     Parses the dataframe containing all of the job posts. The first
     step is to remove companies that are spam, which is mainly
     'Indeed Prime'. Afterwards, duplicate entries are dropped based
     on the 'company', 'date_posted', and 'title' fields. Often times
     there are multiple of the same job posting listed on different days
     which is not useful to search through for the end-user.
     """
    spam_companies = ['Indeed Prime']
    df = df[~df['company'].isin(spam_companies)]
    df = df.drop_duplicates(subset=['company', 'date_posted', 'title'])
    df.title = df.title.str.strip()
    return df


def save_posts(df: pd.DataFrame):
    """
    Saves each dataframe row as a record using Django's get_or_create
    (object only saves if it doesn't already exist)
    """
    records = df.to_dict('records')

    for record in records:
        Company.objects.get_or_create(
            name=record['company'])

        Post.objects.get_or_create(
            title=record['title'],
            company_id=record['company'],
            defaults={
                'date_posted': record['date_posted'],
                'description': record['description'],
                'location': record['location'],
                'is_sponsored': False,
                'date_added_db': record['date_added_db'],
                'source_id': record['source'],
                'link': record['link'],
            }

        )
