from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User as DjangoUser
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views import View

from common.mixins import ViewMixin
from users.forms import UserRegistrationForm, ProfileForm, UserEditForm
from users.models import Profile


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


class Register(View):
    context = {'active': 'signup'}

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if DjangoUser.objects.filter(username=request.POST['username']).exists():
            messages.error(request, 'The user with this username already exists')
        elif user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            profile = Profile(user=new_user,
                              date_of_birth=profile_form.cleaned_data['date_of_birth'])
            if request.FILES:
                profile.photo = request.FILES['photo']
            new_user.save()
            profile.save()
            login(request, new_user)
            return redirect('blogs:posts')
        else:
            messages.error(request, 'Data is not valid.')
        self.context['user_form'] = user_form
        self.context['profile_form'] = profile_form
        return render(request, 'users/register.html', self.context)

    def get(self, request, *args, **kwargs):
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
        self.context['user_form'] = user_form
        self.context['profile_form'] = profile_form
        return render(request, 'users/register.html', self.context)


class Edit(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if request.POST['old_password'] and not check_password(request.POST['old_password'], request.user.password):
            messages.error(request, 'Password is wrong')
        elif user_form.is_valid() and profile_form.is_valid():
            cd = user_form.cleaned_data
            request.user.set_password(cd['new_password'])
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            print(user_form.is_valid())
            print(profile_form.is_valid())
            messages.error(request, 'Error updating your profile')
        return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})

    def get(self, request, *args, **kwargs):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})
