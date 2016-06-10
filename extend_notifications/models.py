from django.db import models
from accounts.models import FiveUser


class RestNotification(models.Model):

    user = models.ForeignKey(
        FiveUser,
        blank=True,
        null=True,
        verbose_name='Кому предназначается уведомление'
    )

    body = models.TextField(
        'Текст уведомления',
        null=True,
        blank=True
    )

    sended = models.BooleanField(
        'Отправлено',
        blank=True,
        default=False
    )
