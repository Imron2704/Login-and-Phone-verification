from django.contrib import admin
from .models import *

admin.site.register(Profile)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'score']


admin.site.register(Messages, MessageAdmin)