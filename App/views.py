from django.shortcuts import render, redirect
from .forms import ContactForm, DonorForm, LoginForm
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


def donor(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your donation!")
            return redirect('donor')  # Redirect to the same page after successful form submission
    else:
        form = DonorForm()
    return render(request, 'donor.html', {'form': form})

def receiver(request):
    return render(request,'receiver.html')

def rveg(request):
    return render(request,'rveg.html')

def rnonveg(request):
    return render(request,'rnonveg.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Login successful!")
            return redirect('login')  # Redirect to the same page after successful form submission
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
        
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
            return redirect('contact')  # Redirect to the same page after successful form submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Create your views here.
