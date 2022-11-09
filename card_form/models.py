from django.db import models

# Create your models here.


class CustomerCard(models.Model):
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    cvc = models.IntegerField()

    def __str__(self):
        name_arr = self.cardholder_name.split('')
        formatted_name = ' '.join([name_arr[0][0], name_arr[1]])
        return formatted_name
