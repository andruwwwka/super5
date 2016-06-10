from django.contrib import admin
from .models import Slide


class SlideAdmin(admin.ModelAdmin):
    pass
admin.site.register(Slide, SlideAdmin)
