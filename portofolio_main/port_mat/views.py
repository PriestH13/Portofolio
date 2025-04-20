from django.shortcuts import render

def home(request):
    return render(request, 'port_mat/home.html')


def about(request):
    return render(request, 'port_mat/about.html')

def projects(request):
    return render(request, 'port_mat/projects.html')

def contact(request):
    return render(request, 'port_mat/contact.html')
