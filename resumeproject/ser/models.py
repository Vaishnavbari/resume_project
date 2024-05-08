from django.db import models
from core.models import home_data
class serv(models.Model):
    
    logo=models.CharField(max_length=200)
    names=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=100)
