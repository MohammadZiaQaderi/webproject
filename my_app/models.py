from django.db import models

# Create your models here.
class Database(models.Model):
    Name=models.CharField(max_length=50)
    DateOfBirth=models.DateField(max_length=30)
    PhoneNumber=models.CharField(max_length=10, editable=True, default=False, unique=True)
    EmailID=models.EmailField(max_length=100, null=False, unique=True, default=False)