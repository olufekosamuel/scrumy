from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.ScrumyUser)
admin.site.register(models.GoalStatus)
admin.site.register(models.ScrumyGoals)