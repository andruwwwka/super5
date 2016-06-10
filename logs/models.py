from django.db import models


class AccessLog(models.Model):

    data = models.TextField(
        u'Данные'
    )

    class Meta:
        verbose_name = u'Лог'
        verbose_name_plural = u'Лог'

    def __str__(self):
        return self.data
