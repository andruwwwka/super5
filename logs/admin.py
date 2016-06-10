from logs.models import AccessLog
from django.contrib import admin


class AccessLogAdmin(admin.ModelAdmin):

    readonly_fields = ['data', ]

admin.site.register(AccessLog, AccessLogAdmin)
