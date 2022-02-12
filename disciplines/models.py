from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField

class Discipline(models.Model):
    """дисциплины"""
    id = ShortUUIDField(
        primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
    )
    name = models.CharField("Имя дисциплины", max_length=150)
    department = models.ForeignKey('departments.Department', verbose_name='Кафедра', on_delete=models.CASCADE,
                                   blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
