from email import message
from unicodedata import name
from django.shortcuts import render
from django.contrib import messages
from .models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def Resume(request):
    messages.success(request, ' the resume.')
    return render(request, 'Resume.html')

def contact(request):
    messages.success(request, 'Welcome To Contact')
    if request.method=='POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        contact = Contact(name=name, email=email, phone=phone, content=content)
        print(name, email, phone, content)
        contact.save()
    return render(request, 'contact.html')

