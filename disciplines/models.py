from django.db import models


class Discipline(models.Model):
    """дисциплины"""
    name = models.CharField("Имя дисциплины", max_length=150, unique=True)
    department = models.ForeignKey('departments.Department', verbose_name='Кафедра', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
