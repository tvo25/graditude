import pytest
from django.conf import settings
from django.urls import reverse, resolve

from graditude.jobs.tests import factories

pytestmark = pytest.mark.django_db


def test_list():
    assert (
        reverse("jobs:list")
        == f"/api/v1/jobs/posts/"
    )


def test_detail():
    post = factories.PostFactory()

    assert (
        reverse("jobs:detail", kwargs={"pk": post.id})
        == f"/api/v1/jobs/posts/{post.id}/"
    )
