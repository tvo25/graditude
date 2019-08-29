from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)


class Source(models.Model):
    NAME_CHOICES = (('Indeed', 'Indeed'),
                    ('LinkedIn', 'LinkedIn'),
                    ('Monster', 'Monster'))
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    from_api = models.BooleanField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    description = models.TextField()
    posted_on = models.DateField()
    added = models.DateField(auto_now_add=True)
    is_sponsored = models.BooleanField()
    source = models.ForeignKey('Source', on_delete=models.CASCADE)
    link = models.URLField()
