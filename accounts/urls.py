from django.conf.urls import url
from accounts.views import RegisterView, LoginView
from django.conf.urls import include

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'accounts.views.logout', name='logout'),
    url(r'', include('athletes.urls')),
]
