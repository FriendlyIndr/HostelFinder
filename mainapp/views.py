from django.shortcuts import render

# Create your views here.

def properties(request):
    context = {}
    return render(request, 'main/Home.html', context) 

def comparison(request):
    context = {}
    return render(request, 'main/Comparison.html', context) 