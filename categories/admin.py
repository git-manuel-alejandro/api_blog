from tabnanny import verbose
from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')

# Register your models here.


admin.site.register(Category, CategoryAdmin)
