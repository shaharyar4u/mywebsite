from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("test", views.test, name='test'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("blog", views.blog, name='blog'),
    path("research", views.research, name='research'),
    path("thought", views.thought, name='thought'),
    path("desacademy", views.desacademy, name='desacademy')
]