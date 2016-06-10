from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from . import models


class ExerciseAdmin(admin.ModelAdmin):
    model = models.Exercise


class RoomInlineAdmin(SuperInlineModelAdmin, TabularInline):
    model = models.TrainingSet
    extra = 0


class HouseInlineAdmin(SuperInlineModelAdmin, StackedInline):
    model = models.Training
    inlines = (RoomInlineAdmin,)
    extra = 0


class OwnerAdmin(SuperModelAdmin):
    inlines = (HouseInlineAdmin,)


admin.site.register(models.Exercise, ExerciseAdmin)
site.register(models.WorkoutDiary, OwnerAdmin)
