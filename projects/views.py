from django.shortcuts import render, get_object_or_404
from .models import project

def home(request):
    return render(request, 'projects/home.html')

def pro(request):
    projects = project.objects
    return render(request, 'projects/project.html', {'projects':projects})

def detail(request, project_id):
    detail_project = get_object_or_404(project, pk = project_id)
    return render(request,'projects/detail.html', {'details':detail_project})
