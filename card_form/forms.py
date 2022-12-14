from django import forms
from django.core.validators import MinLengthValidator
import re
from datetime import date

from .models import CustomerCard

current_year = date.today().year - 2000


def only_numbers(value):
    """
        Checks that value only consists of numbers.
    """
    regex = r"\D"
    if len(re.findall(regex, value)) != 0:
        print(re.findall(regex, value))
        raise forms.ValidationError('Wrong format, numbers only')


def only_letters(value):
    """
        Checks that value only includes latin alphabetical characters.
    """
    regex = r"[^a-zA-z ]"
    if len(re.findall(regex, value)) != 0:
        print(re.findall(regex, value))
        raise forms.ValidationError('Please use valid characters.')


def has_two_parts(value):
    """
        Checks 'cardholder name' consists of two groups of characters separated by a space.
    """
    if len(value.split(' ')) != 2:
        raise forms.ValidationError(
            'Please enter your first name followed by your surname.')


error_messages = {
    "cardholder_name": {
        "required": "Please enter your full name"
    },
    "card_number": {
        "required": "Please enter your card number"
    },
    "expiry_month": {
        "required": "Can't be blank"
    },
    "expiry_year": {
        "required": "Can't be blank"
    },
    "cvc": {
        "required": "Can't be blank"
    }
}


# class CardForm(forms.ModelForm):
#     class Meta:
#         model = CustomerCard
#         fields = '__all__'

#     def clean_expiry_month(self):
#         expiry_month = self.cleaned_data.get('expiry_motnh')

#         if

#     def clean(self):
#         super(CardForm, self).clean()


class CardForm(forms.Form):
    cardholder_name = forms.CharField(
        label="cardholder name",
        max_length=27,
        error_messages=error_messages["cardholder_name"],
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Jane Appleseed'
        }),
        validators=[only_letters, has_two_parts]
    )
    card_number = forms.CharField(
        label="card number",
        max_length=16,
        error_messages=error_messages["card_number"],
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. 1234 5678 9123 0000'}),
        validators=[
            MinLengthValidator(16, message="Card number must be 16 digits."),
            only_numbers,
        ]
    )
    expiry_month = forms.CharField(
        label="exp month",
        max_length=2,
        error_messages=error_messages["expiry_month"],
        widget=forms.TextInput(
            attrs={'placeholder': 'MM'}
        ),
        validators=[
            MinLengthValidator(2,
                               message="Enter a valid month.")
        ]
    )
    expiry_year = forms.CharField(
        label="exp year",
        max_length=2,
        error_messages=error_messages["expiry_year"],
        widget=forms.TextInput(
            attrs={'placeholder': 'YY'}
        ),
        validators=[
            MinLengthValidator(2,
                               message="Enter a valid year.")
        ]
    )
    cvc = forms.CharField(
        label="cvc",
        error_messages=error_messages["cvc"],
        min_length=1,
        max_length=3,
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. 123'}
        ),
        validators=[
            MinLengthValidator(3, message="CVV must be three digits.")
        ]
    )
