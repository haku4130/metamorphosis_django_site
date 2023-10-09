from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Project, Employee, News


def index(request):
    theme = request.GET.get('theme') if request.GET.get('theme') is not None else ''
    template = 'main/projects_list.html'
    projects = Project.objects.filter(
        Q(theme__name__icontains=theme) |
        Q(title__icontains=theme) |
        Q(description__icontains=theme)
    )
    context = {'projects': projects, 'current_theme': theme}
    return render(request, template, context)


def news(request):
    template = 'main/news.html'
    context = {'news': News.objects.all()}
    return render(request, template, context)


def people(request):
    template = 'main/people.html'
    context = {'people': Employee.objects.all()}
    return render(request, template, context)


def about(request):
    template = 'main/about.html'
    return render(request, template)


def contacts(request):
    template = 'main/contacts.html'
    return render(request, template)


def project_detail(request, project_id):
    template = 'main/project_detail.html'
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}
    return render(request, template, context)
