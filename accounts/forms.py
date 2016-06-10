from django import forms

from django.forms.utils import ErrorList

from django.forms import widgets
from django.contrib.auth import get_user_model
from athletes.models import Athlete


class RegistrationForm(forms.Form):

    email = forms.EmailField(
        label='E-Mail',
        widget=widgets.EmailInput(attrs={'placeholder': 'E-Mail', 'autocomplete': 'off'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=widgets.PasswordInput(attrs={'placeholder': 'Пароль', 'autocomplete': 'off'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=widgets.PasswordInput(attrs={'placeholder': 'Подтверждение пароля', 'autocomplete': 'off'})
    )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['width'] = '500px;'

    def clean(self):
        # ToDo: Добавить верификацию email
        # ToDo: Добавить проверку сложности пароля
        if get_user_model().objects.filter(email=self.data['email']).exists():
            self._errors.setdefault('email', ErrorList())
            self._errors['email'] += ['Пользователь уже зарегистрирован в системе']
        password1 = self.data.get("password1")
        password2 = self.data.get("password2")
        if password1 and password2 and password1 != password2:
            self._errors.setdefault('password1', ErrorList())
            self._errors['password1'] += ['Пароли не совпадают']

    def save(self):
        try:
            user = get_user_model().objects.get(email=self.data['email'])
        except get_user_model().DoesNotExist:
            user = get_user_model().objects.create_user(
                email=self.data['email'],
                password=self.data['password1'],
            )
            Athlete.objects.create(user=user)
            user.save()
        self.user = user
        self.str_password = self.data['password1']


# code-review: Базовая форма переопределена только для того что бы поставить
# placeholder???  В моём понимании вся что хранится здесь не должно иметь
# отношение к отрисовки формы, то есть все название и тексты в идеале
# должны находиться в шаблоне у верстальщика или в БД
# code-review-answer: Базовая форма переопределена, в первую очередь, для того,
# чтобы реализовать обработку ошибок формы
# code-review: Я имею в виду почему имено базовую форму, ведь есть встроенные в
# Django формы для логина и авторизации, вот их можно было и переопределить,
# но сейчас такое уже не получится
# code-review-answer: Да, действительно можно было. Почему сейчас не получится?
# code-review: Модель пользователя переопределена, можешь попробовать
# переопределить модели форм сделанные для встроенной модели пользователя
class LoginForm(forms.Form):

    email = forms.EmailField(
        label='e-mail',
        widget=widgets.EmailInput(attrs={'placeholder': 'E-mail', 'type': 'text'})
    )
    password = forms.CharField(
        label=u'Пароль',
        widget=widgets.PasswordInput(attrs={'placeholder': 'Пароль'})
    )

    def clean(self):
        try:
            self.user = get_user_model().objects.get(email=self.data['email'])
        except get_user_model().DoesNotExist:
            self._errors.setdefault('email', ErrorList())
            self._errors['email'] += ['Пользователь не зарегистрирован в системе']

    def save(self):
        self.str_password = self.data['password']
