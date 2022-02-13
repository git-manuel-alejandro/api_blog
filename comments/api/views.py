from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from comments.api.serializers import CommentSerializer
from comments.models import Commet


class CommentsView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Commet.objects.all()
    filter_backends = [OrderingFilter]
    ordering = ['-created_at']
