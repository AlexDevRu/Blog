from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
    path('', Users.as_view(), name='users'),
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('edit/', Edit.as_view(), name='edit'),
    path('my-profile/', profile, name='profile'),
    path('<slug:slug>/', User.as_view(), name='user_detail'),
]
