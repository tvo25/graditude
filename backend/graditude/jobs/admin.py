from django.contrib import admin

from graditude.jobs.models import Company, Position, Post, Source

admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Post)
admin.site.register(Source)
