# Generated by Django 3.1.3 on 2020-11-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codefury_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee',
            field=models.BooleanField(default=True),
        ),
    ]