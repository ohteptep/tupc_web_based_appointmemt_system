# Generated by Django 3.2.8 on 2022-08-17 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20220817_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentform',
            name='yrgraduate',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appointmentform',
            name='yrlevel',
            field=models.CharField(max_length=100),
        ),
    ]
