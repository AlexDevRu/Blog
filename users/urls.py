from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', Users.as_view(), name='users'),
    path('my-profile/', profile, name='profile'),
    path('<slug:slug>/', User.as_view(), name='user_detail'),
]
