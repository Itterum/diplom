from django.db import models


class Gallery(models.Model):
    title = models.CharField('Название галлери', max_length=256)
    description = models.TextField('Описание', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class Photo(models.Model):
    image = models.ImageField('Картинка', upload_to='gallery/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Галлерея')
