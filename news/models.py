from django.db import models
from datetime import date
from django.urls import reverse
import departments.models


class News(models.Model):
    """Новости"""
    name = models.CharField("Имя новости", max_length=150)
    description = models.TextField("Описание")
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField('Фотография', upload_to='department/')
    photos = models.ImageField('Фотографии', upload_to='department/', blank=True,null=True)
    date = models.DateField('Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
