from django.db import models


class ProjectsPhoto(models.Model):
    image = models.ImageField(upload_to='static/projects_photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.image.name


class ProjectTheme(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    theme = models.ForeignKey(ProjectTheme, null=True, on_delete=models.PROTECT)
    photos = models.ManyToManyField(ProjectsPhoto)

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
    pub_date = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(NewsPhoto, blank=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employee_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
