from django.urls import path

from graditude.jobs.api.views import (
    PostDetail,
    PostList
)

app_name = "jobs"
urlpatterns = [
    path("posts/", view=PostList.as_view(), name="list"),
    path("posts/<int:pk>/", view=PostDetail.as_view(), name="detail"),
]
