from .models import RestNotification
from django.http import HttpResponse


def sended(request):
    data = request.GET.get('id')
    notification = RestNotification.objects.get(id=data)
    notification.sended = True
    notification.save()
    return HttpResponse('')
