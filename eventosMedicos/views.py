from django.shortcuts import render
from django.http import HttpResponse

def healthCheck(request):
    return HttpResponse('ok')

# Create your views here.

def index(request):
    return render(request, 'index.html')

def eventos(request):
    return render(request, 'eventos.html')

def contacto(request):
    return render(request, 'contacto.html')