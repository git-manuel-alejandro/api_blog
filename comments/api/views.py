from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentSerializer
from comments.models import Commet


class CommentsView(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Commet.objects.all()
