from django.shortcuts import render
from .models import *
# Create your views here.
def skillview(request):
    user=skills.objects.all()
    return render(request, "edu/skill.html",{"user":user,"skill":"active"})