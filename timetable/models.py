from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField


class Timetable(models.Model):

    NOT_SPECIFIED = 'none'
    PARA = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    VISITTYPE = (
        ('remote', 'Удаленная'),
        ('locale', 'Очная'),
    )
    DISCTYPE = (
        ('lecture', 'Лекция'),
        ('practice', 'Практика'),
        ('laboratory_work', 'Лабораторная работа'),
        ('course_work', 'Курсовая работа'),
        ('diplom_work', 'Дипломная работа'),
        ('assessment', 'Зачет'),
        ('assessment_with_score', 'Зачет с оценкой'),
        ('exam', 'Экзамен'),
    )

    para = models.CharField(
        'Пара', max_length=10, choices=PARA, default=NOT_SPECIFIED
    )

    visit = models.CharField(
        'Тип пары', max_length=10, choices=VISITTYPE, default=NOT_SPECIFIED
    )

    type = models.CharField(
        'Тип занятий', max_length=30, choices=DISCTYPE, default=NOT_SPECIFIED
    )

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