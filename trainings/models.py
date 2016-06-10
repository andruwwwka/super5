from django.utils import timezone
from django.db import models
from athletes.models import Zone, Target
from super5 import settings


class Exercise(models.Model):

    LOW, LOW_MIDDLE, MIDDLE, HEIGHT, VERY_HIGH = 0, 1, 2, 3, 4
    LEVEL = (
        (LOW, 'Низкий'),
        (LOW_MIDDLE, 'Ниже среднего'),
        (MIDDLE, 'Средний'),
        (HEIGHT, 'Высокий'),
        (VERY_HIGH, 'Очень высокий')
    )

    title = models.CharField('Название', max_length=100, default='')
    description = models.TextField('Описание', default='')

    synchronous_vimeo_video_link = models.URLField('Ссылка на синхрон видео на вимео', blank=True, null=True)
    tutorial_vimeo_video_link = models.URLField('Ссылка на объясняющее видео на вимео', blank=True, null=True)

    difficulty = models.IntegerField(verbose_name='Сложность', blank=True, null=True, choices=LEVEL)
    zone = models.ForeignKey(Zone, verbose_name='Группа мышц', blank=True, null=True)
    target = models.ForeignKey(Target, verbose_name='Тип', blank=True, null=True)

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнение'

    def __str__(self):
        return self.title


class WorkoutDiary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = 'Дневник тренировок'
        verbose_name_plural = 'Дневники тренировок'

    def __str__(self):
        return self.user.email

    def get(self):
        pass


class Training(models.Model):
    date = models.DateField(
        'Дата',
        default=timezone.now
    )
    result = models.TextField(
        'Результат',
        default='',
        blank=True,
        null=True
    )
    workout_diary = models.ForeignKey(
        'WorkoutDiary',
        verbose_name='Дневник тринировки'
    )

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return "%s - %s" % (self.workout_diary, self.date)


class TrainingSet(models.Model):
    number_in_training = models.IntegerField(
        'Номер в тренировке'
    )
    exercises = models.ManyToManyField(
        'Exercise',
        verbose_name='Упражнения',
    )
    training = models.ForeignKey(
        'Training',
        verbose_name='Тренировка'
    )

    class Meta:
        verbose_name = 'Сет'
        verbose_name_plural = 'Сеты'

    def __str__(self):
        return str(self.number_in_training)
