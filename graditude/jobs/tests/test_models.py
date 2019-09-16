from typing import TYPE_CHECKING

import pytest

from graditude.jobs.tests.factories import PostFactory, PositionFactory

pytestmark = pytest.mark.django_db


class TestPositionModel:
    def test_search_str(self):
        intern = PositionFactory.build(title='Front End Engineer')

        assert intern.search_str() == 'Front+End+Engineer'


class TestPostModel:
    def test_experience_property(self):
        intern = PostFactory.build(title='Software Engineer Intern')
        full_time = PostFactory.build(title='Software Engineer')

        assert intern.experience == 'Internship'
        assert full_time.experience == 'Full-Time'

    def test_sponsored_property(self):
        post_no_date = PostFactory.build(date_posted=None)
        post_no_location = PostFactory.build(location=None)

        assert post_no_date.sponsored
        assert post_no_location.sponsored

        post_w_date = PostFactory.build()
        post_w_location = PostFactory.build()

        assert not post_w_date.sponsored
        assert not post_w_location.sponsored
