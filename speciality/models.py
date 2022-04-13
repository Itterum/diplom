from django.db import models
from shortuuid.django_fields import ShortUUIDField

from utils.model_utils import generate_id


class Speciality(models.Model):
    """Специальности"""
    id = models.CharField(primary_key=True, max_length=10,
                          unique=True, default=generate_id, editable=False)
    name = models.CharField("имя специальность", max_length=150)
    department = models.ForeignKey('departments.Department', verbose_name="Кафедра", on_delete=models.CASCADE,
                                   blank=True, null=True)
    remote_education_time = models.CharField('Время обучения удалённо', max_length=150)
    locale_education_time = models.CharField('Время обучения очно', max_length=150)
    is_active = models.BooleanField('Активно', default=True)

    def delete(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"
