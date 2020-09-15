from django.views.generic.base import ContextMixin


class ViewMixin(ContextMixin):
    active = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = self.active
        return context
