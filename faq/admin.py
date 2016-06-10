from django import forms
from django.contrib import admin
from django.db.models import Q

from faq.models import Category, Answer, Question


class CategoryAdmin(admin.ModelAdmin):
    pass


class AnswerAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnswerAdminForm, self).__init__(*args, **kwargs)
        self.fields['question'].queryset = Question.objects.filter(answer__isnull=True)
        if self.instance.pk:
            self.fields['question'].queryset = Question.objects.filter(
                Q(answer__isnull=True) |
                Q(id=self.instance.question.pk)
            )
            self.initial['question'] = self.instance.question.pk


class AnswerAdmin(admin.ModelAdmin):
    form = AnswerAdminForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(Answer, AnswerAdmin)
