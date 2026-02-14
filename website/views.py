from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'website/index.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'website/project_detail.html', {'project': project})
