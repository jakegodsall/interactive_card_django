from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CardForm
from .models import CustomerCard

# Create your views here.


def card_form(request):
    # if POST request, then bound Form
    if request.method == 'POST':
        card_form = CardForm(request.POST)

        if card_form.is_valid():
            form_data = card_form.cleaned_data
            print(card_form.cleaned_data)
            customer_data = CustomerCard(
                cardholder_name=form_data["cardholder_name"],
                card_number=form_data["card_number"],
                expiry_month=form_data["expiry_month"],
                expiry_year=form_data["expiry_year"],
                cvc=form_data["cvc"]
            )
            customer_data.save()
            return HttpResponseRedirect('/thank-you')

    # if GET request, then unbound form
    elif request.method == 'GET':
        card_form = CardForm()

    return render(request, 'card_form/card_form.html', {
        "form": card_form
    })


def thank_you(request):
    return render(request, 'card_form/thank_you.html')
