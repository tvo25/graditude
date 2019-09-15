from django.db.models import Q
from rest_framework import generics

from graditude.jobs.models import Post
from graditude.jobs.api.serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.exclude(
        Q(title__icontains='internship') | Q(title__icontains='intern')
    ).select_related()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all().select_related()
    serializer_class = PostSerializer
