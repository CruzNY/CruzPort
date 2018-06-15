from django.shortcuts import render
from .models import project

def home(request):
    return render(request, 'projects/home.html')
def pro(request):
    projects = project.objects
    return render(request, 'projects/project.html', {'projects':projects})
