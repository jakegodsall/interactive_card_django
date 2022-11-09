from django import forms
import re


def only_numbers(value):
    regex = r"\D"
    if len(re.findall(regex, value)) != 0:
        print(re.findall(regex, value))
        raise forms.ValidationError('Wrong format, numbers only')


def only_letters(value):
    regex = r"[^a-zA-z ]"
    if len(re.findall(regex, value)) != 0:
        print(re.findall(regex, value))
        raise forms.ValidationError('Please use valid characters.')


def has_two_parts(value):
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
        validators=[only_numbers]
    )
    expiry_month = forms.IntegerField(
        label="exp month",
        min_value=1,
        max_value=12,
        error_messages=error_messages["expiry_month"],
        widget=forms.NumberInput(
            attrs={'placeholder': 'MM'}
        )
    )
    expiry_year = forms.IntegerField(
        label="exp year",
        min_value=0,
        max_value=22,
        error_messages=error_messages["expiry_year"],
        widget=forms.NumberInput(
            attrs={'placeholder': 'YY'}
        )
    )
    cvc = forms.IntegerField(
        label="cvc",
        error_messages=error_messages["cvc"],
        widget=forms.NumberInput(
            attrs={'placeholder': 'e.g. 123'}
        ))
