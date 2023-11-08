from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ProjectsPhoto(models.Model):
    image = models.ImageField(upload_to='static/projects_photos/')
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    is_main = models.BooleanField(default=False, verbose_name=_("Show as main photo on homepage"))

    def clean(self):
        # Если фотография установлена как основная, убедиться, что нет других фото с is_main=True для этого проекта
        if self.is_main:
            main_photos = ProjectsPhoto.objects.filter(
                is_main=True,
                project_photos__in=Project.objects.filter(photos=self)
            ).exclude(id=self.id)
            if main_photos.exists():
                raise ValidationError(_("There can be only one main photo per project."))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.image.name


class ProjectTheme(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    theme = models.ManyToManyField(ProjectTheme, blank=True)
    photos = models.ManyToManyField(ProjectsPhoto, related_name='project_photos')
    main_photo = models.OneToOneField(ProjectsPhoto, null=True, blank=True, on_delete=models.SET_NULL)

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
