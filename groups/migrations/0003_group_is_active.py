# Generated by Django 3.2 on 2022-04-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20220313_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активно'),
        ),
    ]
