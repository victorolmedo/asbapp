from django.shortcuts import render
from django.http import HttpResponse

def BASE(request):
    return render(request, 'pages/base.html')

def inicio(request):
    return render(request, 'pages/customers.html')
