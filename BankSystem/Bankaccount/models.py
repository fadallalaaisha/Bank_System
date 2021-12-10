from django.db import models

# Create your models here.
class BankAccount(models.Model):
    account_number=models.PositiveIntegerField(max_length=12)
    balance_amount=models.PositiveBigIntegerField()
    deposit=models.PositiveBigIntegerField()
    withdraw=models.PositiveIntegerField(max_length=8)
    code_number=models.CharField(max_length=5)
    loan=models.CharField(max_length=6)
    Repay=models.PositiveIntegerField()
    Customers=models.CharField(max_length=10)
    Transfer=models.PositiveIntegerField()

