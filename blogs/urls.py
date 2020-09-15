from django.urls import path, include
from .views import *

app_name = 'blogs'

urlpatterns = [
    path('', Posts.as_view(), name='posts'),
    path('post/<slug:slug>/', Post.as_view(), name='post'),
    path('tags/', Tags.as_view(), name='tags'),
    path('tag/<slug:slug>/', Tag.as_view(), name='tag'),
    path('users/', include('users.urls'))
]
