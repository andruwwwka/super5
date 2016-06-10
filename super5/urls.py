from django.conf.urls import include, url
from django.contrib import admin

from super5.views import IndexPage, StaticPage
from rest.urls import api_patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset_done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'
    ),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    url(r'^trainings/', include('trainings.urls', namespace="trainings")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^athletes/', include('athletes.urls', namespace="athletes")),
    url(r'^faq/', include('faq.urls', namespace="faq")),
    url(r'^extend_notifications/', include('extend_notifications.urls')),

    url(r'^rest/', include('rest.urls')),
    url(r'^api/', include(api_patterns)),

    url(r'^$', IndexPage.as_view(), name='index_page'),
    url(r'^author/$', StaticPage.as_view(template_name="static/author.html"), name='author'),
    url(r'^for-business/$', StaticPage.as_view(template_name="static/for_business.html"), name='for_business'),
    url(r'^privacy-policy/$', StaticPage.as_view(template_name="static/privacy_policy.html"), name='privacy_policy'),
    url(r'^how-it-works/$', StaticPage.as_view(template_name="static/how_it_works.html"), name='how_it_works'),
    url(r'^contacts/$', StaticPage.as_view(template_name="static/contacts.html"), name='contacts'),

    url(r'^redactor/', include('redactor.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r"^notifications/", include('pinax.notifications.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': "./media/"}),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
