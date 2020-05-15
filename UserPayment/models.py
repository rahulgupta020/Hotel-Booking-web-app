from django.db import models

class UserPaymentdb(models.Model):
    paymentid=models.IntegerField()
    orderid=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    orderamt=models.IntegerField()
    productinfo=models.CharField(max_length=1000)
    paid=models.BooleanField() 