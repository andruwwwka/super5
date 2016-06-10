from django.conf.urls import url

from faq.views import FaqIndexPage

urlpatterns = [
    url(r'^$', FaqIndexPage.as_view(), name='index'),
    url(r'^(?P<category_id>\d+?)$', FaqIndexPage.as_view(), name='category'),
    url(r'^faq_search/(?P<search_field>\w+?)$', 'faq.views.faq_search', name='search'),
]
