from rest_framework import serializers
from comments.models import Commet


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commet
        fields = '__all__'


# s
