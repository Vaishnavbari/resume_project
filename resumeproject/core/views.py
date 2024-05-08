from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from . models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def homeview(request,pk):
    
    {"home":"active"}
    if pk:
     user=home_data.objects.get(pk=pk)
    else:
        return HttpResponse("No id found")
    # if id==1:
    #     user=home.objects.get(id=1)
    # elif id==2:
    #    user=home.objects.get(id=2)
    # elif id==3:
    #    user=home.objects.get(id=3)
    # elif id==4:
    #    user=home.objects.get(id=4)
    # else:
    #     return HttpResponse("No id found")
        
    return render(request,"app/home.html",{"home":"active","user":user})
def contact(request):
    return render(request,"app/contact.html",{"contact":"active"})

# def data(request):
#     if request.method=="POST":
#         name=request.POST['fname']
#         email=request.POST['email']
#         subject=request.POST['subject']
#         your_meassge=request.POST['message']
#         r=contacts.objects.create( 
#                 name=name,
#                 email=email,
#                 subject=subject,
#                 yourmessage=your_meassge
#                 )
#     else:
#         print("method is not post")
  
#     return redirect("contact")

# def data(request):
  
#     if request.method=="POST":
#         fm=registration(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.add_message(request,messages.SUCCESS,"your response send succesfully")
#             fm=registration()
#     else:
#         fm=registration()
#     return render(request,"app/contact.html",{"form":fm ,"contact":"active"})

def contactview(request):

      
   return render(request,"app/contact2.html",{"contact":"active"})

def insertdata(request):
   if request.method=="POST":
      name= request.POST['fname']
      email=request.POST['email']
      subject=request.POST['subject']
      yourmessage=request.POST['message']
      user=contact2.objects.create(name=name,email=email,subject=subject,yourmessage=yourmessage)
      messages.add_message(request,messages.SUCCESS,"your response send succesfully")
   return redirect("contact")