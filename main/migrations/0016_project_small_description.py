# Generated by Django 4.2.5 on 2023-11-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_projectstatus_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='small_description',
            field=models.CharField(default='конкурс', max_length=50),
        ),
    ]
