from datetime import datetime
from multiprocessing import context
from django.http import HttpRequest
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "var1":"Sent var",
        "var2":"sent var2" 
    }
    return render(request,'index.html',context)

def about(request):
    context = {
        "var1":"Sent var",
        "var2":"sent var2" 
    }
    return render(request,'about.html',context)  
    

def heval(request):
    return render(request,'heval.html')

def services(request):
    return render(request,'services.html')
    

def loginUser(request):
    return render(request,'login.html')       

def contact(request):
    if (request.method) == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email ,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent succusfully!')
    return render(request,'contact.html')