from django.db import models

from utils.model_utils import generate_id

from utils.model_utils import generate_id


class News(models.Model):
    """Новости"""
    id = models.CharField(
        primary_key=True, max_length=20, unique=True, default=generate_id, editable=False
    )
    name = models.CharField("Имя новости", max_length=150)
    description = models.TextField("Описание")
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField('Фотография', upload_to='department/')
    photos = models.ImageField('Фотографии', upload_to='department/', blank=True, null=True)
    gallery = models.ForeignKey(
        'gallery.Gallery', on_delete=models.CASCADE, blank=True, null=True,
        verbose_name='Галерея'
    )
    date = models.DateField('Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
