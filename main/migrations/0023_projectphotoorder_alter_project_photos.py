# Generated by Django 4.2.5 on 2023-11-15 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_project_main_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhotoOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projectsphoto')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.project')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('project', 'photo')},
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='photos',
        ),
        migrations.AddField(
            model_name='project',
            name='photos',
            field=models.ManyToManyField(related_name='project_photos', through='main.ProjectPhotoOrder',
                                         to='main.projectsphoto'),
        ),
    ]
