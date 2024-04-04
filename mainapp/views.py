from django.shortcuts import render
from .models import *

# Create your views here.

def properties(request):
    hostels = Hostel.objects.all()
    context = {"hostels":hostels}
    return render(request, 'main/Home.html', context) 

def comparison(request):
    hostels = Hostel.objects.all()
    context = {"hostels":hostels}
    return render(request, 'main/Comparison.html', context) 
