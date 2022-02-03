from django.db import models
from datetime import date
from django.urls import reverse
import departments.models


class Speciality(models.Model):
    """Специальности"""
    name = models.CharField("имя специальность", max_length=150)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"
