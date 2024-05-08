from django.db import models

class skills(models.Model):
    language=models.CharField( max_length=50)
    percentage=models.IntegerField()