from django.shortcuts import redirect, render_to_response
from django.views.generic import TemplateView
from faq.forms import QuestionForm
from faq.models import Category, Answer


class FaqIndexPage(TemplateView):

    template_name = 'faq/index.html'

    def __init__(self):
        super(FaqIndexPage, self).__init__()
        self.categories = Category.objects.all()
        self.answers = Answer.objects.none()
        self.form = QuestionForm()

    def get_context(self, request, **kwargs):
        category_id = kwargs.get('category_id', None)
        if category_id and not self.answers:
            self.answers = Answer.objects.filter(question__category_id=category_id)
        elif self.categories and not self.answers:
            self.answers = Answer.objects.all()
        context = {
            'categories': self.categories,
            'answers': self.answers,
            'form': self.form
        }
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context(request, **kwargs))

    def post(self, request, *args, **kwargs):
        if 'search_field' in request.POST and request.POST['search_field']:
            return redirect('faq:search', search_field=request.POST['search_field'])
        else:
            self.form = QuestionForm(data=request.POST)
            ctx = self.get_context(request, **kwargs)
            if self.form.is_valid():
                self.form.save()
                self.form = QuestionForm()
                ctx.update(
                    {
                        'message': 'Ваш вопрос отправлен нашим специалистам, спасибо!'
                    }
                )
            return self.render_to_response(ctx)


def faq_search(request, search_field):
    answers = Answer.objects.filter(text__icontains=search_field)
    ctx = {
        'answers': answers,
        'message': 'Результаты поиска по запросу "%s"' % search_field,
        'categories': Category.objects.all(),
        'form': QuestionForm()
    }
    return render_to_response('faq/index.html', ctx)
