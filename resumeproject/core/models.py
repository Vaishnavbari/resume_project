from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class contacts(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    yourmessage=models.CharField(max_length=1150)
    
    def  __str__(self):
        return self.name + self.email
    
    
class home(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
class home_data(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)   
    # options=(
    #     ("seo","seo"),
    #      ('webdev',"webDev"),
    #     ('webdesign',"webdrsign")
    # )    
    # services= models.CharField( max_length=50,
    #     choices=options,
    # )
    
    
class contact2(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    yourmessage=models.CharField(max_length=1150)
