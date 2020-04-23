from django.contrib import admin
from .models import Notice
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display = ['subject','date']
admin.site.register(Notice, NoticeAdmin)