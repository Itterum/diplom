# Generated by Django 3.2 on 2022-04-10 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0008_department_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='is_active',
        ),
    ]
