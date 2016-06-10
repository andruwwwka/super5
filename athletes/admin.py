from django.contrib import admin
from .models import Athlete, TargetPriority, ZonePriority


class TargetPriorityInLine(admin.TabularInline):
    model = TargetPriority
    extra = 0


class ZonePriorityInLine(admin.TabularInline):
    model = ZonePriority
    extra = 0


class AthleteAdmin(admin.ModelAdmin):
    inlines = [
        TargetPriorityInLine,
        ZonePriorityInLine,
    ]
admin.site.register(Athlete, AthleteAdmin)


class TargetAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Target, TargetAdmin)


class ZoneAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Zone, ZoneAdmin)
