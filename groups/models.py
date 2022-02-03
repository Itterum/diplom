from django.db import models
import uuid


class Group(models.Model):
    """Группы"""
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])
    code = models.CharField('Код группы', max_length=150)
    email = models.CharField('Почта группы', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    spec = models.ForeignKey('speciality.Speciality', related_name='Speciality', verbose_name='Специальность',
                             on_delete=models.CASCADE, blank=True,
                             null=True)
    headmen = models.ForeignKey('profiles.Profile', related_name='headmen', verbose_name='Староста',
                                on_delete=models.CASCADE, blank=True,
                                null=True)
    curator = models.ForeignKey('profiles.Profile', related_name='curator', verbose_name='Куратор',
                                on_delete=models.CASCADE, blank=True,
                                null=True)
    start_date = models.DateField('Начало обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
