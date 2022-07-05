from django.contrib import admin
from .models import *

admin.site.register(Task)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'deadline', 'done',)
