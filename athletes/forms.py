from django import forms
from utils.widgets import CustomTextField
from django.forms.utils import ErrorList
from .models import Athlete, TargetPriority, ZonePriority


class PersonalDataForm(forms.ModelForm):

    TITLE = u'Основные данные'

    class Meta:
        model = Athlete
        fields = ['email', 'height', 'width', 'gender', 'birthday', 'training_duration', 'level', 'week_day']

    email = forms.EmailField(
        label='E-Mail',
        widget=CustomTextField(placeholder='E-Mail'),
        required=False
    )

    height = forms.IntegerField(
        label='Рост, см.',
        widget=CustomTextField(placeholder='Рост, см.'),
        required=False
    )
    width = forms.IntegerField(
        label='Вес, кг.',
        widget=CustomTextField(placeholder='Вес, кг.'),
        required=False
    )
    gender = forms.ChoiceField(
        label='Пол',
        choices=Athlete.GENDER,
        required=False
    )
    level = forms.ChoiceField(
        label='Уровень подготовки',
        choices=Athlete.LEVEL,
        required=False
    )
    training_duration = forms.ChoiceField(
        label='Продолжительность тренировок',
        choices=Athlete.DURATION,
        required=False
    )
    birthday = forms.DateField(
        label='Дата рождения',
        required=False
    )
    week_day = forms.MultipleChoiceField(
        label='Дни недели',
        choices=Athlete.WEEK_DAYS,
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(PersonalDataForm, self).__init__(*args, **kwargs)
        if self.instance.user.email:
            self.initial['email'] = self.instance.user.email
        self.fields['birthday'].widget.attrs['class'] = 'datepicker'
        self.birthday_title = self.instance.birthday_value

    def get_days_count(self, level=None, training_duration=None):
        COUNT_MAP = {
            0: 3,
            1: 3,
            2: 4,
            3: 5,
            4: 5,
        }
        count = 5
        duration = training_duration or self.instance.training_duration
        if duration and duration > 1:
            if level is not None:
                count = COUNT_MAP[level]
            elif self.instance.level:
                count = COUNT_MAP[self.instance.level]
        return count

    def clean(self):
        week_days_list = self.cleaned_data.get('week_day')
        level_param = self.cleaned_data.get('level', None)
        if level_param:
            level = int(level_param)
            training_duration = int(self.cleaned_data.get('training_duration'))
            if week_days_list and len(week_days_list) != self.get_days_count(
                    level=level,
                    training_duration=training_duration
            ):
                self._errors.setdefault('week_day', ErrorList())
                self._errors['week_day'] += [
                    'Вы выбрали некорректное число дней. Необходимо выбрать %s' % self.get_days_count(
                        level=level,
                        training_duration=training_duration
                    )]

    def save(self, commit=True):
        super(PersonalDataForm, self).save(commit=True)
        if self.cleaned_data.get('email', None):
            self.instance.user.email = self.cleaned_data['email']
            self.instance.user.save()


class TargetPriorityForm(forms.Form):

    TITLE = u'Приоритет целей'

    PREFIX = 'priority'

    target_model = TargetPriority

    def __init__(self, *args, **kwargs):
        super(TargetPriorityForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial')

        athlete = initial.get('athlete')
        self.targets = athlete.get_targets().values_list(
            "target_priority__id",
            "target_priority__name"
        )

    def save(self):
        pass


class ZonePriorityForm(forms.Form):
    TITLE = u'Приоритет зон'
    PREFIX = 'zone'

    zone_model = ZonePriority

    def __init__(self, *args, **kwargs):
        super(ZonePriorityForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        athlete = initial.get('athlete')
        self.targets = athlete.get_zones().values_list(
            "zone_priority__id",
            "zone_priority__name"
        )

    def save(self):
        pass


class WizardFormSteps(PersonalDataForm):
    def save(self, commit=True):
        new_instance = self._meta.model.objects.get(id=self.instance.id)
        for field in self.fields:
            if field != 'email':
                setattr(new_instance, field, getattr(self.instance, field))
        self.instance = new_instance
        super(WizardFormSteps, self).save(commit=True)


class PriorityWizardFormStep1(WizardFormSteps):

    TITLE = u'Биометрические параметры'

    def __init__(self, *args, **kwargs):
        super(PriorityWizardFormStep1, self).__init__(*args, **kwargs)
        del self.fields['birthday']
        del self.fields['training_duration']
        del self.fields['level']
        del self.fields['week_day']


class PriorityWizardFormStep2(WizardFormSteps):

    TITLE = 'Дата рождения'

    def __init__(self, *args, **kwargs):
        super(PriorityWizardFormStep2, self).__init__(*args, **kwargs)
        del self.fields['email']
        del self.fields['height']
        del self.fields['width']
        del self.fields['gender']
        del self.fields['training_duration']
        del self.fields['level']
        del self.fields['week_day']


class PriorityWizardFormStep3(WizardFormSteps):

    TITLE = u'Продолжительность тренировки, уровень подготовки'

    def __init__(self, *args, **kwargs):
        super(PriorityWizardFormStep3, self).__init__(*args, **kwargs)
        del self.fields['email']
        del self.fields['height']
        del self.fields['width']
        del self.fields['gender']
        del self.fields['birthday']
        del self.fields['week_day']


class PriorityWizardFormStep6(WizardFormSteps):

    TITLE = 'Дни недели'

    def __init__(self, *args, **kwargs):
        super(PriorityWizardFormStep6, self).__init__(*args, **kwargs)
        del self.fields['email']
        del self.fields['height']
        del self.fields['width']
        del self.fields['gender']
        del self.fields['training_duration']
        del self.fields['level']
        del self.fields['birthday']


class SimpleFieldForm(PersonalDataForm):

    TITLE = u'Введите значение поля'

    def __init__(self, data, *args, **kwargs):
        super(SimpleFieldForm, self).__init__(data, *args, **kwargs)
        field = data.get('field', None)
        for form_field in self.fields:
            if form_field != field:
                del self.fields[form_field]
