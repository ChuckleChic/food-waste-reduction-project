from django.shortcuts import render , HttpResponse
from datetime import datetime
from App.models import Contact
from App.models import login
from django.contrib import messages

# Create your views here.
            
def index(request):
    context = {
        
        }
    return render(request,'index.html' , context)
     # return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page") 
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page") 
def receiver(request):
    return render(request,'receiver.html')
def donor(request):
    return render(request,'donor.html')
def login(request):
    return render(request,'login.html')
    if request.method == "POST" :
        name = request.POST.get('Full name')
        product = request.POST.get('Product name')
        mobile = request.POST.get('Mobile number')
        location = request.POST.get('location')
        quantity = request.POST.get('quantity')
        login = login(name=name, product=product , mobile=mobile,location=location,quantity=quantity)
        login.confirm()
        messages.success(request, "Your message has been sent!")
        
def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email , desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
        
    return render(request,'contact.html' )

# Create your views here.
