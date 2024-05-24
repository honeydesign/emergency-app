from django.db import models

# Create your models here.
class Form(models.Model):
    full_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.full_name
