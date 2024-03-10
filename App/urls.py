from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("", views.index , name='home'),
    path("about", views.about , name='about'),
    path("receiver", views.Executive , name='receiver'),
     path("donor", views.donor , name='donor'),
    path("services", views.services , name='services'),
    path("contact", views.contact , name='contact'),
]
