# Generated by Django 4.0.4 on 2022-04-27 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='on_going',
            field=models.BooleanField(default=False),
        ),
    ]
