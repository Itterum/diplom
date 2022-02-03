from django.db import models
import uuid


class Group(models.Model):
    """Кафедры"""
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])
    code = models.CharField('Код группы', max_length=150)
    email = models.CharField('Почта группы', max_length=50,blank=True, null=True)
    phone_number = models.CharField('Номер телефона', max_length=50)
    headmen = models.ForeignKey('profiles.Profile',verbose_name='Headmen', on_delete=models.CASCADE, blank=True, null=True)
    curator = models.ForeignKey('profiles.Profile',verbose_name='Curator', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
