# Generated by Django 3.2.2 on 2021-05-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='arrival_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='starting_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
