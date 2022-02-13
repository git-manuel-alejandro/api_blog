from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly
from posts.models import Post


class PostView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(published=False)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__slug']
    # filterset_fields = ['category']
