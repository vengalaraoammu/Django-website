from django.db import models

# Create your models here.
class friends_List(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    WhatsappNumber=models.CharField(max_length=100)
    Phone_Number=models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name
