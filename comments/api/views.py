from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from comments.api.serializers import CommentSerializer
from comments.models import Commet
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAnCreateOnly


class CommentsView(ModelViewSet):
    permission_classes = [IsOwnerOrReadAnCreateOnly]
    serializer_class = CommentSerializer
    queryset = Commet.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    filter_fields = ['post']
