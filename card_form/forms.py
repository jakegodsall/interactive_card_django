from django import forms

error_messages = {
    "cardholder_name": {
        "required": "Please enter your full name"
    },
    "card_number": {
        "required": ""
    },
    "expiry_month": {

    },
    "expiry_year": {

    },
    "cvc": {

    }
}


class CardForm(forms.Form):
    cardholder_name = forms.CharField(
        label="cardholder name",
        max_length=100,
        error_messages=error_messages["cardholder_name"],
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Jane Appleseed'})
    )
    card_number = forms.CharField(
        label="card number",
        max_length=16,
        error_messages=error_messages["card_number"],
        widget=forms.TextInput(
            attrs={'placeholder': 'e.g. 1234 5678 9123 0000'})
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
