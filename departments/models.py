from django.db import models
import uuid


class Department(models.Model):
    """Кафедры"""
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])
    name = models.CharField('Название кафедры', max_length=150)
    email = models.CharField('Почта', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    manager_department = models.OneToOneField(
        'profiles.Profile',
        related_name='manager_department',
        on_delete=models.SET_NULL, null=True
    )
    description = models.TextField('Описание')
    photo = models.ImageField('Фотография', upload_to='department/', blank=True)
    photos = models.ImageField('Фотографии', upload_to='department/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
