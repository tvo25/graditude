import pytest
from rest_framework.authtoken.models import Token

from graditude.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_create_auth_token():
    """
    Test the create_auth_token signal to ensure that a token is
    generated after a new user is created.
    """
    user = UserFactory()

    try:
        Token.objects.get(user=user)
    except Token.DoesNotExist:
        pytest.fail("Token does not exist")
