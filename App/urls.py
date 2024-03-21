from django.contrib import admin
from django.urls import path
from App import views
from . import views

urlpatterns = [
    path("", views.index , name='home'),
    path("services", views.services , name='services'),
    path("about", views.about , name='about'),
     path('contact/', views.contact, name='contact'),
    path('donor/', views.donor, name='donor'),
    path('login/', views.login, name='login'),
    path("receiver", views.receiver , name='receiver'),
    path("rveg", views.rveg , name='rveg'),
    path("rnonveg", views.rnonveg , name='rnonveg'),
    
   
   
]


