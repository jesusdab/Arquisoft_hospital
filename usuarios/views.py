from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task, Doctor
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("hello world %s" % username)

def about(request):
    return HttpResponse("about page")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request):
    return HttpResponse("tasks")

def doctores(request):
    doctors = list(Doctor.objects.values())
    return render(request, 'doctores.html', 
                  {'doctores': doctors})