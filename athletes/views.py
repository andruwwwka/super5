from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView
from rest_framework import generics, mixins, permissions
from rest_framework.response import Response
from .forms import (
    PersonalDataForm, ZonePriorityForm,
    TargetPriorityForm, SimpleFieldForm
)
from .models import Athlete, TargetPriority, ZonePriority
from .serializations import (
    AthleteSerializer, TargetPrioritySerializer, ZonePrioritySerializer,
    AthleteAllDataSerializer
)


class PersonalData(TemplateView):

    template_name = "personal_data_simple_form.html"

    def get_context(self, request, *args, **kwargs):
        context = {
            'form': self.form,
            'target_form': self.target_form,
            'zone_form': self.zone_form
        }
        return context

    def get(self, request, *args, **kwargs):
        if hasattr(request.user, 'athlete'):
            instance = request.user.athlete
        else:
            instance = Athlete(
                user=request.user
            )
            instance.save()
        self.target_form = TargetPriorityForm(
            initial={'athlete': instance}
        )
        self.zone_form = ZonePriorityForm(
            initial={'athlete': instance}
        )
        self.form = PersonalDataForm(instance=instance)
        return self.render_to_response(self.get_context(request))

    def post(self, request, *args, **kwargs):
        self.target_form = TargetPriorityForm(
            initial={'athlete': request.user.athlete}
        )
        self.zone_form = ZonePriorityForm(
            initial={'athlete': request.user.athlete}
        )
        if Athlete.objects.filter(user=request.user).exists():
            instance = Athlete.objects.get(user=request.user)
        else:
            instance = Athlete(user=request.user)
            instance.save()
        self.form = PersonalDataForm(data=request.POST, instance=instance)
        if self.form.is_valid():
            self.form.save()
            self.form = PersonalDataForm(instance=self.form.instance)
        return self.render_to_response(self.get_context(request))


class PersonalDataWizardView(SessionWizardView):

    template_name = 'personal_data_master_form.html'

    def done(self, form_list, **kwargs):
        for form in form_list:
            if form.is_valid():
                form.save()
        return redirect('athletes:personal_data')

    def get_form_instance(self, step):
        if step in ['0', '1', '2', '5']:
            if Athlete.objects.filter(user=self.request.user).exists():
                instance = Athlete.objects.get(user=self.request.user)
            else:
                instance = Athlete(user=self.request.user)
                instance.save()
            return self.instance_dict.get(step, instance)
        return self.instance_dict.get(step, None)

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        initial.update({'athlete': self.request.user.athlete})
        return initial


def change_priority(request):
    data = request.GET.get('data')
    items = data.split(';')
    targets_id = [item.split('_')[1] for item in items if 'priority_' in item]
    zones_id = [item.split('_')[1] for item in items if 'zone_' in item]

    for priority, item_id in enumerate(targets_id, 1):
        TargetPriority.change(request.user.athlete, priority, id=item_id)

    for priority, item_id in enumerate(zones_id, 1):
        ZonePriority.change(request.user.athlete, priority, id=item_id)

    return JsonResponse({'success': True})


class ChangeSomeField(TemplateView):

    template_name = "personal_data_simple_form.html"

    def get_context(self, request, *args, **kwargs):
        context = {
            'form': self.form,
        }
        super(ChangeSomeField, self).get_context(request)
        return context

    def get(self, request, *args, **kwargs):
        field = kwargs.get('field', None)
        try:
            instance = Athlete.objects.get(user=request.user)
        except TypeError:
            return HttpResponseRedirect("/accounts/login/")
        self.form = SimpleFieldForm(instance=instance, data={'field': field, })
        return self.render_to_response(self.get_context(request))

    def post(self, request, *args, **kwargs):
        field = kwargs.get('field', None)
        instance = Athlete.objects.get(user=request.user)
        data = request.POST
        data.update(
            {
                'field': field
            }
        )
        self.form = SimpleFieldForm(data=data, instance=instance)
        if self.form.is_valid():
            self.form.save()
        return redirect('athletes:personal_data')


class AthleteAPI(generics.RetrieveUpdateAPIView):
    serializer_class = AthleteSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Athlete

    def get_object(self):
        user = self.request.user
        athlete, created = self.model.objects.get_or_create(user=user)
        return athlete


class AthleteAllDataAPI(AthleteAPI):
    serializer_class = AthleteAllDataSerializer


class TargetPriorityAPI(mixins.ListModelMixin, mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    """Используется для отображения, создания и обновления целей"""
    serializer_class = TargetPrioritySerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = TargetPriority

    def get_queryset(self):
        user = self.request.user
        athlete, created = Athlete.objects.get_or_create(user=user)
        return athlete.get_targets()

    def update(self, request, *args, **kwargs):
        athlete = request.user.athlete
        priority_list = request.data
        for priority in priority_list:
            level = priority['priority']
            slug = priority['target_priority']['slug']
            self.model.change(athlete, level, slug=slug)
        queryset = athlete.targetpriority_set.all()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ZonePriorityAPI(mixins.ListModelMixin, mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    """Используется для отображения, создания и обновления приоритетных зон"""
    serializer_class = ZonePrioritySerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = ZonePriority

    def get_queryset(self):
        user = self.request.user
        athlete, created = Athlete.objects.get_or_create(user=user)
        return athlete.get_zones()

    def update(self, request, *args, **kwargs):
        athlete = request.user.athlete
        priority_list = request.data
        for priority in priority_list:
            level = priority['priority']
            slug = priority['zone_priority']['slug']
            self.model.change(athlete, level, slug=slug)
        queryset = athlete.zonepriority_set.all()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
