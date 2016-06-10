from django.db import models


class Slide(models.Model):

    photo = models.ImageField('Файл фото', blank=True, upload_to='./media/upload_images')
    link = models.URLField('Ссылка', blank=True)
    title = models.CharField('Заголовок', blank=True, max_length=511)
    under_title = models.CharField('Подзаголовок', blank=True, max_length=511)
    body = models.TextField('Текст слайда', blank=True)

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title

    def photo_or_link(self):
        return self.photo.name or self.link
