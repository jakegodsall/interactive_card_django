from django.shortcuts import render

# Create your views here.


def card_form(request):
    return render(request, 'card_form/card_form.html')


def thank_you(request):
    return render(request, 'card_form/thank_you.html')
