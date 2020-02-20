from django.contrib import admin
from .models import tasks,assined_task
# Register your models here.
admin.site.register(tasks)
admin.site.register(assined_task)
