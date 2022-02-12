from rest_framework.viewsets import ModelViewSet
from posts.api.serializers import PostSerializer
from posts.models import Post


class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=False)
    lookup_field = 'slug'
