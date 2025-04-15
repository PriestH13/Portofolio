from django.shortcuts import render

def home(request):
    return render(request, 'port_mat/home.html')