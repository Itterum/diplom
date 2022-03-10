from django.db import models

from utils.model_utils import generate_id


class Group(models.Model):
    """Группы"""

    NOT_SPECIFIED = 'none'
    VISITTYPE = (
        ('remote', 'Удаленная'),
        ('locale', 'Очная'),
    )

    id = models.CharField(primary_key=True, max_length=10, unique=True, default=generate_id)
    code = models.CharField('Код группы', max_length=150)
    email = models.CharField('Почта группы', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50, blank=True, null=True)
    spec = models.ForeignKey('speciality.Speciality', related_name='Speciality', verbose_name='Специальность',
                             on_delete=models.CASCADE, blank=True,
                             null=True)
    headmen = models.ForeignKey('profiles.Profile', related_name='headmen', verbose_name='Староста',
                                on_delete=models.CASCADE, blank=True,
                                null=True)
    curator = models.ForeignKey('profiles.Profile', related_name='curator', verbose_name='Куратор',
                                on_delete=models.CASCADE, blank=True,
                                null=True)
    visit_type = models.CharField('Тип группы', max_length=10, choices=VISITTYPE, default=NOT_SPECIFIED, blank=True, null=True)
    start_date = models.DateField('Начало обучения')
    is_session = models.BooleanField('Началась ли сессия?', default=False)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
