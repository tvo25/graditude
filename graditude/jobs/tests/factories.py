from django.utils import timezone

import factory

from graditude.jobs import models


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Company

    name = factory.Faker('company')


class SourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Source

    name = 'LinkedIn'
    from_api = False


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    title = factory.Faker('job')
    company = factory.SubFactory(CompanyFactory)
    description = factory.Faker('sentence')
    location = f"{factory.Faker('city')}, {factory.Faker('country')}"
    is_sponsored = False
    date_posted = timezone.now()
    date_added_db = timezone.now()
    source = factory.SubFactory(SourceFactory)
    link = factory.Faker('url')
