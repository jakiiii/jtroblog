from django import forms

from apps.contact.models import Contact


class ContactCreationForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'body',
        )
