from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import CardForm
from .models import CustomerCard

# Create your views here.


def format_cardnumber(card_number):
    formatted = ''
    indices = range(0, 13, 4)
    for idx in indices:
        block = card_number[idx:idx+4]
        formatted += ' ' + ''.join(block)
    return formatted.strip()


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

            request.session["cardholder_name"] = form_data["cardholder_name"]
            request.session["card_number"] = format_cardnumber(
                form_data["card_number"])
            request.session["expiry_month"] = form_data["expiry_month"]
            request.session["expiry_year"] = form_data["expiry_year"]
            request.session["cvc"] = form_data["cvc"]

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
        context["cardholder_name"] = self.request.session["cardholder_name"]
        context["card_number"] = self.request.session["card_number"]
        context["expiry_month"] = self.request.session["expiry_month"]
        context["expiry_year"] = self.request.session["expiry_year"]
        context["cvc"] = self.request.session["cvc"]
        return context
