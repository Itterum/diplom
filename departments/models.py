from django.db import models

from .validators import validate_file_extension

from utils.model_utils import generate_id


class Department(models.Model):
    """Кафедры"""
    id = models.CharField(primary_key=True, max_length=10,
                          unique=True, default=generate_id)
    name = models.CharField('Название кафедры', max_length=150)
    email = models.CharField('Почта', max_length=50, blank=True, null=True)
    phone_number = models.CharField(
        'Номер телефона', max_length=50, blank=True, null=True)
    address = models.CharField('Адрес', max_length=100, blank=True, null=True)
    manager_department = models.OneToOneField(
        'profiles.Profile',
        related_name='manager_department',
        verbose_name="Заведущий кафедры",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    description = models.TextField('Описание', blank=True, null=True)
    basic_timetable_department = models.FileField(
        'Основное рассписание', upload_to='timetable-d/',
        blank=True, null=True,
        validators=[validate_file_extension]
    )
    session_timetable_department = models.FileField(
        'Рассписание сессии', upload_to='timetable-d/', blank=True, null=True,
        validators=[validate_file_extension])
    session_absentia_timetable_department = models.FileField(
        'Рассписание сессии заочно', upload_to='timetable-d/', blank=True,
        null=True)
    photo = models.ImageField(
        'Фотография', upload_to='department/', blank=True, null=True)
    photos = models.ImageField(
        'Фотографии', upload_to='department/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding is False:
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            new = self
            changed_fields = []
            for field in cls._meta.get_fields():
                field_name = field.name
                try:
                    if getattr(old, field_name) != getattr(new, field_name):
                        changed_fields.append(field_name)
                except Exception as ex:
                    pass
            kwargs['update_fields'] = changed_fields
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"
