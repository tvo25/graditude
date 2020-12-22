import uuid as uuid_lib

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # Used by the API to look up the record
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
