from django.contrib import admin
from blogs.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'user']
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
