from rest_framework import generics
from extend_notifications.models import RestNotification
from rest.serializers import NotificationSerializer, DayWeekSerializer
from athletes.models import Athlete
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.settings import api_settings

from .serializers import UserSerializer


class NotificationList(generics.ListCreateAPIView):
    model = RestNotification
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user_id = int(self.request.QUERY_PARAMS['user_pk'])
        notifications = self.model.objects.filter(user_id=user_id, sended=False)
        return notifications


class DayWeekAPI(generics.RetrieveUpdateAPIView):
    serializer_class = DayWeekSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Athlete

    def get_object(self):
        user = self.request.user
        athlete, created = self.model.objects.get_or_create(user=user)
        return athlete


class UserRegisterViewSet(viewsets.ViewSet):
    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        pass

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}
        pass
