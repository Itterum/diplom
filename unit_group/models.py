# import uuid
# from datetime import date
#
# from django.db import models
# from shortuuid.django_fields import ShortUUIDField
#
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# class Profile(models.Model):
#     MALE = 'M'
#     FEMALE = 'F'
#     NOT_SPECIFIED = 'NS'
#     GENDER = (
#         ('M', 'Мужской'), ('F', 'Женский'), ('NS', 'Не указан')
#     )
#
#     id = ShortUUIDField(
#         primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
#     full_name = models.CharField('ФИО', max_length=150)
#     first_name = models.CharField('Имя', max_length=50, editable=False)
#     last_name = models.CharField('Фамилия', max_length=50, editable=False)
#     gender = models.CharField(
#         max_length=10, choices=GENDER, default=NOT_SPECIFIED
#     )
#     birth_date = models.DateField(null=True, blank=True)
#     email = models.CharField('Почта', max_length=50, editable=False)
#     phone_number = models.CharField('Номер телефона', max_length=50)
#     address = models.CharField('Адрес', max_length=100)
#     photo = models.ImageField('Фотография', upload_to='users/', blank=True)
#     # type_user = models.
#
#     def __str__(self):
#         return f'{self.user}'
#
#     class Meta:
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Профили'
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#
#
# class TeacherGroup(models.Model):
#     '''преподаватель'''
#     id = ShortUUIDField(
#         primary_key=True, length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
#     )
#     position = models.CharField('Должность', max_length=50)
#     qualification = models.CharField('Квалификация', max_length=50)
#     # supervisor_group_id = models.ForeignKey()
#
#     def __str__(self):
#         return self.position
#
#     class Meta:
#         verbose_name = 'Преподаватель'
#         verbose_name_plural = 'Преподаватели'
#
#
# class DepartmentDuplicate(models.Model):
#     id = models.CharField(primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False)
#
#     name = models.CharField('Название кафедры', max_length=150)
#     email = models.CharField('Почта', max_length=50)
#     phone_number = models.CharField('Номер телефона', max_length=50)
#     address = models.CharField('Адрес', max_length=100)
#     number_of_groups = models.PositiveIntegerField('Количество групп', default=0)
#     number_of_specialties = models.PositiveIntegerField('Количество групп', default=0)
#     manager_department = models.ForeignKey(
#         TeacherGroup, verbose_name='Заведующий кафедры', on_delete=models.SET_NULL, null=True
#     )
#     description = models.TextField('Описание')
#     photo = models.ImageField('Фотография', upload_to='department/')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Кафедра'
#         verbose_name_plural = 'Кафедры'
#
#
# class StudentGroup(models.Model):
#     '''студенты'''
#     FULL_TIME = 'FT'
#     PART_TIME = 'PT'
#     NOT_SPECIFIED = 'NS'
#     EDUC_TYPE = (
#         ('FT', 'Очное'), ('PT', 'Заочное'), ('NS', 'Не указано')
#     )
#
#     id = models.CharField(
#         primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
#     )
#     group_number = models.CharField('Номер группы', max_length=20)
#     course_number = models.CharField('Номер курса', max_length=10)
#     headman = models.BooleanField('Староста', default=False)
#     phone_number_parents = models.CharField('Контактный телефон родителей', max_length=50)
#     education_type = models.CharField(
#         max_length=2, choices=EDUC_TYPE, default=NOT_SPECIFIED
#     )
#     cathedra_id = models.ForeignKey(
#         DepartmentDuplicate, verbose_name='Кафедра', on_delete=models.SET_NULL, null=True
#     )
#
#     def __str__(self):
#         return self.group_number
#
#     class Meta:
#         verbose_name = 'Студент'
#         verbose_name_plural = 'Студенты'
#
#
# class GroupsDuplicate(models.Model):
#     id = models.CharField(
#         primary_key=True, max_length=10, unique=True, default=uuid.uuid4().hex[:10], editable=False
#     )
#     group_number = models.CharField('Номер группы', max_length=150)
#     number_of_students = models.CharField('Количество студентов', max_length=50)
#     headman = models.ForeignKey(
#         StudentGroup, verbose_name='Староста', on_delete=models.SET_NULL, null=True
#     )
#     name_of_specialty = models.CharField('Специальность', max_length=100)
#
#     def __str__(self):
#         return self.group_number
#
#     class Meta:
#         verbose_name = 'Группа'
#         verbose_name_plural = 'Группы'
