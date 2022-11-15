from django.urls import path

from .views import CardFormView, thank_you

urlpatterns = [
    path('', CardFormView.as_view(), name="card_form"),
    path('thank-you', thank_you, name="thank_you")
]
