from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, HttpResponse

from home.models import Contact


# Create your views here.
def index(request):
    context = {"brand_name": "Shreyas"}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        contact_obj = Contact(name=name, password=password, date=datetime.today())
        contact_obj.save()
        messages.success(request, 'Your info is sent successfully !')
    return render(request, 'contact.html')
