from django.contrib import admin
from users.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
