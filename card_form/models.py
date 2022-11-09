from django.db import models

# Create your models here.


class CustomerCard(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    cvc = models.IntegerField()

    def __str__(self):
        split_name = self.cardholder_name.split(' ')
        return ' '.join([f"{split_name[0][0]}.", split_name[1]])
