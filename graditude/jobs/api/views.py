from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import AllowAny

from graditude.jobs.models import Post
from graditude.jobs.api.serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.exclude(
        Q(title__icontains='internship') | Q(title__icontains='intern')
    ).select_related()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all().select_related()
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
