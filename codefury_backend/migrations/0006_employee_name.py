# Generated by Django 3.1.3 on 2020-11-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codefury_backend', '0005_employee_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]