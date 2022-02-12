from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostSerializer
from posts.models import Post
from posts.api.permissions import IsAdminOrReadOnly


class PostView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=False)
    lookup_field = 'slug'
