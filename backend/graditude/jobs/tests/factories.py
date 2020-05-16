from django.utils import timezone

import factory

from graditude.jobs import models


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Company
        django_get_or_create = ("name",)

    name = factory.Faker("company")


class SourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Source
        django_get_or_create = ("name",)

    name = "LinkedIn"
    from_api = False


class PositionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Position
        django_get_or_create = ("title",)

    title = factory.Faker("job")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post
        django_get_or_create = ("title",)

    title = factory.Faker("job")
    company = factory.SubFactory(CompanyFactory)
    description = factory.Faker("sentence")
    location = f"{factory.Faker('city')}, {factory.Faker('country')}"
    is_sponsored = False
    date_posted = timezone.now()
    date_added_db = timezone.now()
    source = factory.SubFactory(SourceFactory)
    link = factory.Faker("url")
