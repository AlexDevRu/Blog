from django import forms
from django.contrib.auth.models import User

from common.mixins import CleanMixin
from users.models import Profile


def set_classes(fields):
    for name, field in fields.items():
        if field.label:
            field.widget.attrs.update({'class': 'form-control',
                                       'placeholder': field.label})
        else:
            field.widget.attrs.update({'class': 'form-control',
                                       'placeholder': ' '.join(list(map(str.title, name.split('_'))))})


class UserRegistrationForm(forms.ModelForm, CleanMixin):
    password = forms.CharField(label='Create password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_classes(self.fields)
        self.fields['first_name'].widget.required = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm, CleanMixin):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput())
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_classes(self.fields)
        self.fields['first_name'].widget.required = True

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_classes(self.fields)
        self.fields['photo'].widget.attrs.update({'class': 'custom-file-input', 'id': 'customFile'})

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
