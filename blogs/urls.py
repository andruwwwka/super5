from django.conf.urls import url
from blogs.views import FeedView

urlpatterns = [
    url(r'^$', FeedView.as_view(), name='feed'),
]
