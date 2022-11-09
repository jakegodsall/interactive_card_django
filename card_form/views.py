from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CardForm

# Create your views here.


def card_form(request):
    # if POST request, then bound Form
    if request.method == 'POST':
        card_form = CardForm(request.POST)

        if card_form.is_valid():
            print(card_form.cleaned_data)

            return HttpResponseRedirect('/thank-you')

    # if GET request, then unbound form
    elif request.method == 'GET':
        card_form = CardForm()

    return render(request, 'card_form/card_form.html', {
        "form": card_form
    })


def thank_you(request):
    return render(request, 'card_form/thank_you.html')
