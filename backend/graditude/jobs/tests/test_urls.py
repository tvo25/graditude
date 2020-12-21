import pytest
from django.urls import reverse

from graditude.jobs.tests import factories

pytestmark = pytest.mark.django_db


def test_list():
    assert reverse("jobs:list") == "/api/v1/jobs/posts/"


def test_detail():
    post = factories.PostFactory()
    result = reverse("jobs:detail", kwargs={"pk": post.id})
    assert result == f"/api/v1/jobs/posts/{post.id}/"
