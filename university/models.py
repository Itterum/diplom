from django.db import models
import shortuuid, uuid
from datetime import date

from shortuuid.django_fields import ShortUUIDField


class Teachers(models.Model):
    '''преподаватель'''
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])

    full_name = models.CharField('ФИО', max_length=150)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birthday = models.CharField('Дата рождения', max_length=50)
    email = models.CharField('Почта', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    photo = models.ImageField('Фотография', upload_to='teachers/')
    position = models.CharField('Должность', max_length=50)
    qualification = models.CharField('Квалификация', max_length=50)

    # supervisor_group_id = models.ForeignKey()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Department(models.Model):
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])

    name = models.CharField('Название кафедры', max_length=150)
    email = models.CharField('Почта', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    number_of_groups = models.PositiveIntegerField('Количество групп', default=0)
    number_of_specialties = models.PositiveIntegerField('Количество групп', default=0)
    manager_department = models.ForeignKey(
        Teachers, verbose_name='Заведующий кафедры', on_delete=models.SET_NULL, null=True
    )
    description = models.TextField('Описание')
    photo = models.ImageField('Фотография', upload_to='department/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class Students(models.Model):
    '''студенты'''
    # EDUC_TYPE = (
    #     ('FT', 'Очное'),
    #     ('PT', 'Заочное'),
    # )
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])


    full_name = models.CharField('ФИО', max_length=150)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birthday = models.DateField('Дата рождения', default=date.today)
    group_number = models.CharField('Номер группы', max_length=20)
    course_number = models.CharField('Номер курса', max_length=10)
    headman = models.BooleanField('Староста', default=False)
    email = models.CharField('Почта', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    phone_number_parents = models.CharField('Контактный телефон родителей', max_length=50)
    # education_type = models.CharField(max_length=2, choices=EDUC_TYPE)
    photo = models.ImageField('Фотография', upload_to='students/')

    cathedra_id = models.ForeignKey(
        Department, verbose_name='Кафедра', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Groups(models.Model):
    id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10])

    group_number = models.CharField('Номер группы', max_length=150)
    number_of_students = models.CharField('Количество студентов', max_length=50)
    headman = models.ForeignKey(
        Students, verbose_name='Староста', on_delete=models.SET_NULL, null=True
    )
    name_of_specialty = models.CharField('Специальность', max_length=100)

    def __str__(self):
        return self.group_number

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
