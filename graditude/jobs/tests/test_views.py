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

        for i in range(100):
            factories.PostFactory()
        count = models.Post.objects.count()

        response = self.client.get(list_url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == count

    def test_detail(self):
        post = factories.PostFactory()
        detail_url = reverse('jobs:detail', kwargs={'pk': post.id})

        response = self.client.get(detail_url)
        assert response.json().get('title') == post.title
