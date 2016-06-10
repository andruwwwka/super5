from django.db import models
from redactor.fields import RedactorField
from super5 import settings


class Post(models.Model):
    head = models.CharField(
        u'Заголовок поста',
        max_length=255
    )
    body = RedactorField(verbose_name=u'Тело поста')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=u'Автор поста'
    )
    post_date = models.DateTimeField(
        u'Дата поста'
    )
    photo = models.ImageField(
        'Фото для главной страницы (опционально)',
        upload_to='./media/upload_images',
        null=True,
        blank=True
    )
    show_in_main = models.BooleanField(
        'Показывать на главной странице',
        default=False
    )
    show_in_feed = models.BooleanField(
        'Показывать в основной ленте блога',
        default=False
    )
    video = models.URLField(
        'Ссылка на видео (опционально)',
        blank=True,
        null=True
    )
    title_main = models.CharField(
        'Заголовок для главной страницы (опционально)',
        max_length=511,
        null=True,
        blank=True
    )
    body_main = models.CharField(
        'Текст для главной страницы (опционально)',
        max_length=511,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

    def __str__(self):
        return u'%s - %s' % (self.head, self.post_date)
