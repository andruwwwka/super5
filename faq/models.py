from django.db import models


class Category(models.Model):

    name = models.CharField(
        'Наименование категории',
        max_length=255,
    )

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

    def __str__(self):
        return self.name


class Question(models.Model):

    category = models.ForeignKey(
        Category,
        verbose_name=u'Категория',
        null=True,
        blank=True
    )
    email = models.EmailField(
        u'Электроннная почта',
        null=True,
        blank=True
    )
    text = models.TextField(
        u'Текст вопроса'
    )

    def __str__(self):
        return u'%s - %s' % (self.category.name, self.text)


class Answer(models.Model):

    question = models.OneToOneField(
        Question,
        verbose_name=u'Вопрос'
    )
    text = models.TextField(
        u'Текст ответа'
    )

    class Meta:
        verbose_name = u'Ответы'
        verbose_name_plural = u'Ответ'

    def __str__(self):
        return u'%s - %s' % (self.question.category.name, self.question.text)
