from django.db import models
from .managers import AccountManager

class Account(models.Model):
    owner = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    objects = AccountManager() 

    def __str__(self):
        return f"{self.owner} — {self.balance}₸"

