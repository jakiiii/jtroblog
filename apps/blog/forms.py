from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Submit, HTML


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=32)
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(EmailPostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-md-12 col-12 mb-1'),
                css_class='row',
            ),
            Row(
                Column('email', css_class='col-md-12 col-12 mb-1'),
                css_class='row',
            ),
            Row(
                Column('to', css_class='col-md-12 col-12 mb-1'),
                css_class='row',
            ),
            Row(
                Column('comments', css_class='col-md-12 col-12 mb-1'),
                css_class='row',
            ),
            Row(
                Div(Submit('submit', 'Submit'), css_class="mt-4"),
            )
        )
