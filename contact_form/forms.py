from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        required=True,
        max_length=50
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=50
    )
    message = forms.CharField(
        required=True,
        label="Message",
        widget=forms.Textarea,
        max_length=250,
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
