from django import forms

from faq.models import Question, Category
from utils.widgets import CustomTextField


class QuestionForm(forms.ModelForm):

    email = forms.EmailField(
        widget=CustomTextField(placeholder='Super5 Email адрес')
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True
    )

    class Meta:
        model = Question
        fields = ['email', 'category', 'text']

    def __init__(self, **kwargs):
        super(QuestionForm, self).__init__(**kwargs)
        self.fields['text'].widget.attrs['class'] = 'textarea_field'
