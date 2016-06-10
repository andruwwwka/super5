from django.views.generic import TemplateView
from itertools import groupby
from .models import Post


MONTHS = [u'Январь', u'Февраль', u'Март', u'Апрель', u'Май', u'Июнь', u'Июль', u'Август', u'Сентябрь',
          u'Октябрь', u'Ноябрь', u'Декабрь']


class FeedView(TemplateView):
    template_name = 'blogs/feed.html'

    def get(self, request, *args, **kwargs):
        archive = list()
        posts = Post.objects.all()
        grouped_by_year = groupby(posts, key=lambda posts: posts.post_date.year)
        for year, values in grouped_by_year:
            year_dict = dict()
            year_posts = list()
            grouped_posts = list(values)
            group_by_month = groupby(grouped_posts, key=lambda grouped_posts: MONTHS[grouped_posts.post_date.month - 1])
            for month, items in group_by_month:
                month_dict = dict()
                list_items = list(items)
                month_dict.update(
                    {
                        'month': month,
                        'count': len(list_items),
                        'month_posts': list_items
                    }
                )
                year_posts.append(month_dict)
            year_dict.update(
                {
                    'year': year,
                    'year_posts': year_posts
                }
            )
            archive.append(year_dict)
        context = {
            'posts': Post.objects.all(),
            'archive': archive
        }
        super(FeedView, self).get(request)
        return self.render_to_response(context)
