from xml.dom.minidom import Comment
from django.contrib import admin
from comments.models import Commet

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'post', 'created_at']


admin.site.register(Commet)
