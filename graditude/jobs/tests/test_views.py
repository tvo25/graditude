from typing import TYPE_CHECKING

import pytest
from django.urls import reverse
from rest_framework import status

from graditude.jobs import models
from graditude.jobs.tests import factories

if TYPE_CHECKING:
    from django.test import Client

pytestmark = pytest.mark.django_db


class TestJobsAPI:
    @pytest.fixture(autouse=True)
    def setUp(self, client: 'Client'):
        self.client = client

    def test_list(self):
        list_url = reverse('jobs:list')

        posts = factories.PostFactory.create_batch(20)

        response = self.client.get(list_url)

        assert response.status_code == status.HTTP_200_OK

        # Check that there are Post objects being returned
        assert len(response.data) > 0

    def test_detail(self):
        post = factories.PostFactory()
        detail_url = reverse('jobs:detail', kwargs={'pk': post.id})

        response = self.client.get(detail_url)
        assert response.json().get('title') == post.title
