# Generated by Django 2.0.1 on 2018-06-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olufekoscrumy', '0002_remove_scrumygoals_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalstatus',
            name='status',
            field=models.IntegerField(choices=[(1, 'Weekly Task'), (2, 'Daily Task'), (3, 'Verified'), (4, 'Done')]),
        ),
    ]
