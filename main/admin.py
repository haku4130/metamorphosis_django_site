from django.contrib import admin
from .models import Project, Employee, News, ProjectsPhoto, NewsPhoto, ProjectTheme

admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(News)
admin.site.register(ProjectsPhoto)
admin.site.register(NewsPhoto)
admin.site.register(ProjectTheme)
