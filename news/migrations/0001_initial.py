# Generated by Django 3.1 on 2022-03-10 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя новости')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='department/', verbose_name='Фотография')),
                ('photos', models.ImageField(blank=True, null=True, upload_to='department/', verbose_name='Фотографии')),
                ('date', models.DateField(verbose_name='Дата рождения')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]