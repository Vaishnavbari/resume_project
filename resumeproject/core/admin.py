from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(contacts)
class contactsadmin(admin.ModelAdmin):
    list_display=["name","email","subject","yourmessage"]