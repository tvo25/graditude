import pandas as pd
from datetime import date

import pytest
from celery.result import EagerResult

from graditude.jobs.models import Post
from graditude.jobs.tasks import IndeedScraper, scrape_indeed
from graditude.jobs.tests.factories import PositionFactory, SourceFactory


@pytest.mark.django_db
def test_scrape_indeed(settings):
    """A basic test to execute the scrape_indeed Celery task."""
    settings.CELERY_TASK_ALWAYS_EAGER = True
    # Create the position
    PositionFactory(title='Software Engineer')
    SourceFactory(name='LinkedIn')

    # Check successful task invoke
    pages = list(range(0, 101, 10))
    task_result = scrape_indeed.delay(pages)
    assert isinstance(task_result, EagerResult)

    # Check that post objects exist
    assert Post.objects.exists()


@pytest.mark.django_db
class TestIndeedScraper:

    def test_scrape(self):
        # Create the position
        PositionFactory(title='Software Engineer')
        SourceFactory(id=1, name='LinkedIn')

        # Check successful task invoke
        pages = list(range(0, 101, 10))

        scraper = IndeedScraper(pages)
        scraper.scrape()
        scraper.save_posts()
        assert Post.objects.exists()

    def test_parse_posts(self):
        scraper = IndeedScraper()
        today = date.today()

        posts = [
            {
                'title': 'Software Engineer',
                'company': 'Graditude',
                'description': "Looking for Python expert",
                'location': 'San Jose, CA',
                'is_sponsored': False,
                'date_posted': today,
                'date_added_db': today,
                'source': 'Indeed',
                'link': 'graditude.herokuapp.com',
                'position': 'Full-time'
            },
            {
                'title': 'Back End Engineer',
                'company': 'Indeed Prime',
                'description': "Write some REST APIs in Django!",
                'location': 'San Franciso, CA',
                'is_sponsored': False,
                'date_posted': today,
                'date_added_db': today,
                'source': 'Indeed',
                'link': 'graditude.herokuapp.com',
                'position': 'Full-time'
            },
            {
                'title': 'Front End Engineer',
                'company': None,
                'description': "You love QA?",
                'location': 'Santa Clara, CA',
                'is_sponsored': False,
                'date_posted': today,
                'date_added_db': today,
                'source': 'Indeed',
                'link': 'graditude.herokuapp.com',
                'position': 'Full-time'
            }
        ]
        for index, post in enumerate(posts):
            scraper.df = scraper.df.append(post, ignore_index=True)

        scraper.parse_posts()

        # Check no spam companies
        assert not ((scraper.df['company']) == 'Indeed Prime').any()

        # Check no null companies
        assert not scraper.df['company'].isnull().values.any()

        # Check no duplicates
        duplicates_exist = scraper.df.duplicated(
            subset=['company', 'date_posted', 'title'])[0]
        assert not duplicates_exist
