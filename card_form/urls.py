from django.urls import path

from .views import CardFormView, ThankYouView

urlpatterns = [
    path('', CardFormView.as_view(), name="card_form"),
    path('thank-you', ThankYouView.as_view(), name="thank_you")
]
