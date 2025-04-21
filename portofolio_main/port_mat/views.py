from django.shortcuts import render
from .models import Projects
from django.shortcuts import get_object_or_404,render

def home(request):
    projects = Projects.objects.all()[:3]
    return render(request, 'port_mat/home.html', {'projects': projects}) 


def about(request):
    return render(request, 'port_mat/about.html')

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'port_mat/projects.html', {'projects': projects})

def contact(request):
    return render(request, 'port_mat/contact.html')
