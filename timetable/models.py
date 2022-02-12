from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField


class Timetable(models.Model):
    id = ShortUUIDField(
        primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
    )
    date = models.DateTimeField()
    discipline = models.ForeignKey('disciplines.Discipline', related_name='Discipline', verbose_name='Дисциплина',
                             on_delete=models.CASCADE, blank=True,
                             null=True)
    teacher = models.ForeignKey('profiles.Profile', related_name='Profile', verbose_name='Преподаватель',
                             on_delete=models.CASCADE, blank=True,
                             null=True)
    department = models.ForeignKey('departments.Department', related_name='Department', verbose_name='Кафедра',
                             on_delete=models.CASCADE, blank=True,
                             null=True)
    group = models.ForeignKey('groups.Group', related_name='Group', verbose_name='Группа',
                             on_delete=models.CASCADE, blank=True,
                             null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"


# Поля модели рассписания
# Дата
# Пара по времени. То что бы показывало какая по счету пара.
# Реализовать через enum
# 1 пара или 2 или 3
# Дисциплина через foreignkay
# Преподаватель через foreignkay
# Кафедра через foreignkay
# Группа через foreignkay
#
# Для уникальности каждому foreignkay
# Добавь уникальные releted_name
# И verbose_name это лейбл
#
# Type - тип занятия:
# Экзамен
# Зачёт
# Зачёт с оценкой
# Практика
# Лобараторная работа
# Курсовая работа
# Лекция
#
# Вид проведения :
# Удалено
# Очно
#
# Все что через через foreignkay
# Blank=true, null=true.