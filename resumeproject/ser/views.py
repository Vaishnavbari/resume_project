from django.shortcuts import render
from .models import *
# Create your views here.
def serviceview(request):
    user=serv.objects.all()
 
    return render( request,"serv/services.html",{"user":user,"services":"active"})