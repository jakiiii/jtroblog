from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=32)
    to = forms.EmailField(max_length=32)
    title = forms.CharField(max_length=255)
    comments = forms.CharField(required=False, widget=forms.Textarea)
