from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^diary/$', 'trainings.views.training_diary_current_month', name='diary_now'),
    url(r'^diary/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', views.DiaryTrainingsView.as_view(), name='diary'),
    url(r'^training/$', views.TrainingView.as_view(), name='training'),
]
