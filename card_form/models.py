from django.db import models

# Create your models here.


class CustomerCard(models.Model):
    id = models.AutoField(primary_key=True)
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    cvc = models.IntegerField()

    def __str__(self):
        return self.cardholder_name
