from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import NotificationList, DayWeekAPI, UserRegisterViewSet
from accounts.views import UserView
from athletes.views import AthleteAPI, ZonePriorityAPI, TargetPriorityAPI, AthleteAllDataAPI
from trainings.views import TrainingsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'training', TrainingsViewSet, base_name='training')
router.register(r'register-user', UserRegisterViewSet, base_name='register-user')

urlpatterns = [
    url(r'^extend_notifications/$', NotificationList.as_view(), name='notification-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

rest_v1_patterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^user/$', UserView.as_view()),
    url(r'^user/day_week/$', DayWeekAPI.as_view()),
    url(r'^user/info/$', AthleteAPI.as_view()),
    url(r'^user/all_info/$', AthleteAllDataAPI.as_view()),
    url(r'^user/target/$', TargetPriorityAPI.as_view()),
    url(r'^user/zone/$', ZonePriorityAPI.as_view()),
    url(r'^routed/', include(router.urls)),
]

api_patterns = [
    url(r'^v1/', include(rest_v1_patterns)),
]
