from django.conf.urls import url

from .forms import (
    TargetPriorityForm, ZonePriorityForm,
    PriorityWizardFormStep1, PriorityWizardFormStep2,
    PriorityWizardFormStep3,
    PriorityWizardFormStep6)
from .views import PersonalData, PersonalDataWizardView, ChangeSomeField
from .views import change_priority

urlpatterns = [
    url(r'^personal-data/$', PersonalData.as_view(), name='personal_data'),
    url(r'^personal-data-master/$',
        PersonalDataWizardView.as_view([PriorityWizardFormStep1, PriorityWizardFormStep2,
                                        PriorityWizardFormStep3, TargetPriorityForm, ZonePriorityForm,
                                        PriorityWizardFormStep6]),
        name='personal_data_master'),
    url(r'^personal-data-master/change_priority/$', change_priority, name='change_priority'),
    url(r'^personal-data/change_priority/$', change_priority, name='change_priority_lk'),
    url(r'^personal-data/(?P<field>\w+)/$', ChangeSomeField.as_view(), name='change_field'),
]
