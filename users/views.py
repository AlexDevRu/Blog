from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from common.mixins import ViewMixin


class Users(ListView, ViewMixin):
    template_name = 'users/users.html'
    context_object_name = 'users'
    active = 'users'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return DjangoUser.objects.exclude(id=self.request.user.id)
        return DjangoUser.objects.all()


class User(DetailView, ViewMixin):
    model = DjangoUser
    slug_field = 'username'
    template_name = 'users/user_detail.html'
    context_object_name = 'user'
    active = 'users'


@login_required
def profile(request):
    return render(request, 'users/user_detail.html', {'user': request.user, 'active': 'profile'})
