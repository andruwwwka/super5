from django.views.generic import TemplateView
from .models import Slide
from blogs.models import Post


class IndexPage(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        ctx = {
            'slides': Slide.objects.all(),
            'posts': Post.objects.filter(show_in_main=True)
        }
        return self.render_to_response(ctx)


class StaticPage(TemplateView):
    def __init__(self, template_name):
        self.template_name = template_name
        super(StaticPage, self).__init__()
