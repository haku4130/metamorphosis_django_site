# Generated by Django 4.2.5 on 2023-11-10 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_projectsphoto_is_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.projectstatus'),
        ),
    ]