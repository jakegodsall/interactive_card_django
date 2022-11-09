from django import forms


class CardForm(forms.Form):
    cardholder_name = forms.CharField(label="cardholder name", max_length=100)
    card_number = forms.CharField(label="card number", max_length=16)
    expiry_month = forms.IntegerField(
        label="exp month", min_value=1, max_value=12)
    expiry_year = forms.IntegerField(
        label="exp year", min_value=0, max_value=22)
    cvc = forms.IntegerField(label="cvc", min_value=0, max_value=999)
