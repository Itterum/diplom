from django.db import models


class Discipline(models.Model):
    """дисциплины"""
    name = models.CharField("Имя дисциплины", max_length=150)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"
