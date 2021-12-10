from django.db import models

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    id=models.CharField(max_length=8,primary_key=True)
    phone_number=models.CharField(max_length=10)
    eamil=models.EmailField(max_length=20)
    username=models.CharField(max_length=8)
    password=models.CharField(max_length=12)

