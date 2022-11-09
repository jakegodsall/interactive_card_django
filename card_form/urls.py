from django.urls import path

from .views import card_form, thank_you

urlpatterns = [
    path('', card_form, name="card_form"),
    path('thank-you', thank_you, name="thank_you")
]
