from django import forms
from django.views.generic.base import ContextMixin


class ViewMixin(ContextMixin):
    active = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = self.active
        return context


class CleanMixin:
    def clean_first_name(self):
        cd = self.cleaned_data
        if not cd['first_name']:
            raise forms.ValidationError('First name is empty.')
        return cd['first_name']
