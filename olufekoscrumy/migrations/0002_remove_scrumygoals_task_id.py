# Generated by Django 2.0.1 on 2018-06-22 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olufekoscrumy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumygoals',
            name='task_id',
        ),
    ]
