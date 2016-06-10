from django.conf.urls import url
from .views import sended

urlpatterns = [
    url(r'^sended/$', sended, name='sended'),
]
