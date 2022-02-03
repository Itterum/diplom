import uuid
from django.db import models
from shortuuid.django_fields import ShortUUIDField

from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Profile(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    NOT_SPECIFIED = 'none'
    GENDER = (
        ('male', 'Мужской'), ('female', 'Женский'), ('none', 'Не указан')
    )

    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    EDUC_TYPE = (
        ('full_time', 'Очная'), ('part_time', 'Заочная'), ('none', 'Не указано')
    )

    STUDENT = 'student'
    TEACHER = 'teacher'
    USER_TYPE = (
        ('student', 'Студент'), ('teacher', 'Преподаватель'), ('none', 'Не указано')
    )

    id = ShortUUIDField(
        primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
    )
    full_name = models.CharField('ФИО', max_length=150)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    gender = models.CharField(
        'Пол', max_length=10, choices=GENDER, default=NOT_SPECIFIED
    )
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    email = models.EmailField('Почта', unique=True)
    phone_number = models.CharField('Номер телефона', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    photo = models.ImageField('Фотография', upload_to='users/', blank=True)
    user_type = models.CharField(
        'Тип пользователя', max_length=10, choices=USER_TYPE, default=NOT_SPECIFIED, blank=True, null=True
    )
    department = models.ForeignKey('departments.Department',
                                   on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey('groups.Group', verbose_name='Group', related_name='group',
                              on_delete=models.CASCADE, blank=True, null=True)

    # поля для студентов
    phone_number_parents = models.CharField('Контактный телефон родителей', max_length=50, blank=True, null=True)
    educ_type = models.CharField(
        'Форма обучения', max_length=10, choices=EDUC_TYPE, default=NOT_SPECIFIED, blank=True, null=True
    )

    # поля преподаветелей
    teacher = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )
    position = models.CharField('Должность', max_length=50, blank=True, null=True)
    qualification = models.CharField('Квалификация', max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
