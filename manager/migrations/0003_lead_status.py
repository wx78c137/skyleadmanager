# Generated by Django 4.0.4 on 2022-04-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_task_on_going'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
