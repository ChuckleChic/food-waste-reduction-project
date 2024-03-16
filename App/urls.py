from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("", views.index , name='home'),
    path("services", views.services , name='services'),
    path("about", views.about , name='about'),
    path("contact", views.contact , name='contact'),
    path("login", views.login , name='login'),
    path("receiver", views.receiver , name='receiver'),
    path("donor", views.donor , name='donor'),
   
   
   
]
