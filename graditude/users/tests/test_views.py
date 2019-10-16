import pytest
from factory import Faker
from rest_framework import status
from rest_framework.test import APIClient

from django.urls import reverse
from django.forms.models import model_to_dict

from graditude.users.models import User
from graditude.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserDetail:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.url = reverse('user-detail', kwargs={"uuid": self.user.uuid})

        self.new_first_name = "Tom"
        self.payload = {'first_name': self.new_first_name}

    def test_get_user(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_put_update_user_unauthorized(self):
        response = self.client.put(self.url, self.payload)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        user = User.objects.get(pk=self.user.id)
        assert user.first_name != self.new_first_name

    def test_put_update_user_authorized(self):
        # Include an appropriate `Authorization:` header on all requests.
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

        response = self.client.put(self.url, self.payload)
        assert response.status_code == status.HTTP_200_OK

        user = User.objects.get(pk=self.user.id)
        assert user.first_name == self.new_first_name


class TestUserCreateViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = APIClient()
        self.url = reverse('user-list')
        self.user_data = model_to_dict(UserFactory.build())

        # Fields set as None, which cannot be serialized as JSON
        self.user_data.pop('id')
        self.user_data.pop('last_login')

    def test_post_invalid_fail(self):
        response = self.client.post(self.url, {})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_post_valid_success(self):
        response = self.client.post(self.url, self.user_data)
        assert response.status_code == status.HTTP_201_CREATED

        user = User.objects.get(pk=response.data.get('id'))
        assert user.username == self.user_data.get("username")
        assert user.check_password(self.user_data.get("password")) is True
