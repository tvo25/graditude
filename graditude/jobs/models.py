from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Source(models.Model):
    NAME_CHOICES = (('Indeed', 'Indeed'),
                    ('LinkedIn', 'LinkedIn'),
                    ('Monster', 'Monster'))
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    from_api = models.BooleanField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey('Company', to_field='name', on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255, null=True)
    is_sponsored = models.BooleanField()
    date_posted = models.DateField(null=True)
    date_added_db = models.DateField(auto_now_add=True)
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    link = models.TextField()

    class Meta:
        unique_together = (('company', 'title', 'date_posted'))
