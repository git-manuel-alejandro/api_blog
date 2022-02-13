from rest_framework.permissions import BasePermission
from comments.models import Commet


class IsOwnerOrReadAnCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Commet.objects.get(pk=id_comment)

            id_user = request.user.pk
            id_user_comment = comment.user_id

            if id_user == id_user_comment:
                return True

            return False
