from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    balance = models.FloatField()

class transfer_history(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    amount = models.FloatField()
