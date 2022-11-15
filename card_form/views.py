from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import CardForm
from .models import CustomerCard

# Create your views here.


class CardFormView(View):
    def post(self, request):
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

    def get(self, request):
        card_form = CardForm()

        return render(request, 'card_form/card_form.html', {
            "form": card_form
        })


class ThankYouView(TemplateView):
    template_name = 'card_form/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
