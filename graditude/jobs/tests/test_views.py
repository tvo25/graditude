from typing import TYPE_CHECKING

import pytest
from django.urls import reverse
from rest_framework import status

from graditude.jobs.tests import factories

if TYPE_CHECKING:
    from django.test import Client

pytestmark = pytest.mark.django_db


class TestJobsAPI:
    @pytest.fixture(autouse=True)
    def setUp(self, client: 'Client'):
        self.client = client
        self.post = factories.PostFactory()
        self.list_url = reverse('jobs:list')
        self.detail_url = reverse('jobs:detail', kwargs={'pk': self.post.id})

    def test_list(self):
        for i in range(100):
            factories.PostFactory()
        response = self.client.get(self.list_url)

        assert response.status_code == status.HTTP_200_OK

        # Test that there are 101 items in the JSON response
        # 100 being within this test, and the 1 extra object form the
        # setup
        assert len(response.data) == 101

    def test_detail(self):
        response = self.client.get(self.detail_url)
        assert response.json().get('title') == self.post.title
