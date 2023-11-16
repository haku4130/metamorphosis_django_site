from django.db import models
from django.utils import timezone


class ProjectsPhoto(models.Model):
    image = models.ImageField(upload_to='static/projects_photos/')
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.image.name


class ProjectStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProjectTheme(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    small_description = models.CharField(max_length=50, default='конкурс')
    theme = models.ManyToManyField(ProjectTheme, blank=True)
    status = models.ForeignKey(ProjectStatus, null=True, blank=True, on_delete=models.SET_NULL)
    main_image = models.ImageField(upload_to='static/projects_photos/', default='static/project_photos/рен1.jpg')
    photos = models.ManyToManyField(ProjectsPhoto, related_name='project_photos')
    location = models.CharField(max_length=100, default='Испания')
    space = models.CharField(max_length=50, default='площадь')
    full_space = models.CharField(max_length=50, default='общая площадь')
    years = models.CharField(max_length=50, default='года')
    client = models.CharField(max_length=50, default='клиент')
    team = models.CharField(max_length=50, default='команда')

    def __str__(self):
        return self.title


class NewsPhoto(models.Model):
    image = models.ImageField(upload_to='static/news_photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.image.name


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    photo = models.OneToOneField(NewsPhoto, null=True, blank=True, unique=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='static/employee_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
