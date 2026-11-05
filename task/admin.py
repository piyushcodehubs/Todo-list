from django.contrib import admin
from .models import Task

# Register your models here.


@admin.register(Task)
class taskview(admin.ModelAdmin):
  list_display=('task','created_at')
  ordering = ('-created_at',)