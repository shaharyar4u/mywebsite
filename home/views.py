from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Registration
from django.contrib import messages
from home import views
import pyrebase

'''
config={
    "apiKey": "AIzaSyCvXtcDeOBT9usvgM5UzI2CEqIK0m_IBb4",
    "authDomain": "shaharyar-s-website.firebaseapp.com",
    "databaseURL": "https://shaharyar-s-website-default-rtdb.firebaseio.com",
    "projectId": "shaharyar-s-website",
    "storageBucket": "shaharyar-s-website.appspot.com",
    "messagingSenderId": "86423165052",
    "appId": "1:86423165052:web:1387db470c3a6d116b11f9",
  }
        firebase=pyrebase.initialize_app(config)
        authe=firebase.auth()
        database=firebase.database()

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    }
    channel_name=database.child('Name').get().val()
    channel_department = database.child('dapartment').get().val()
    channel_designation = database.child('designation').get().val()
    return render(request, 'index.html', {
        "channel_name"=channel_name,
        "channel_designation" = channel_designation,
        "channel_department" = channel_department
    })
    # return HttpResponse("this is homepage")
'''
def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def research(request):
    return render(request, 'research.html')

def thought(request):
    return render(request, 'thought.html')

def blog(request):
    return render(request, 'blog.html')

def desacademy(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        regd = Registration(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        regd.save()
        messages.success(request, 'Your registration is successful!')
    return render(request, 'desacademy.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

