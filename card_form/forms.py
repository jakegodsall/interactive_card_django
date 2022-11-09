from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
import re
from datetime import date

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


class CardForm(forms.Form):
    cardholder_name = forms.CharField(
        label="cardholder name",
        max_length=100,
        error_messages=error_messages["cardholder_name"],
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Jane Appleseed'}),
        validators=[only_letters, has_two_parts]
    )
    card_number = forms.CharField(
        label="card number",
        max_length=16,
        error_messages=error_messages["card_number"],
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. 1234 5678 9123 0000'}),
        validators=[
            only_numbers,
            MinLengthValidator(16, message="Card number must be 16 digits.")
        ]
    )
    expiry_month = forms.IntegerField(
        label="exp month",
        error_messages=error_messages["expiry_month"],
        widget=forms.NumberInput(
            attrs={'placeholder': 'MM'}
        ),
        validators=[
            MinValueValidator(1, message="Enter a valid month."),
            MaxValueValidator(12, message="Enter a valid month.")
        ]
    )
    expiry_year = forms.IntegerField(
        label="exp year",
        error_messages=error_messages["expiry_year"],
        widget=forms.NumberInput(
            attrs={'placeholder': 'YY'}
        ),
        validators=[
            MinValueValidator(current_year, message="Enter a valid year."),
            MaxValueValidator(current_year + 50, message="Enter a valid year.")
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
