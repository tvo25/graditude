from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from graditude.users.models import User
from graditude.users.api.permissions import IsUserOrReadOnly
from graditude.users.api.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    """
    Updates and retrieves user accounts
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)
    lookup_field = "uuid"


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates user accounts
    """

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
