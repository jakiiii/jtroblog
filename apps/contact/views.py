from django.shortcuts import render
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = "Contact"
        return context
