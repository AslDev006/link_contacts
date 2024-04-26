from django.contrib import admin
from .models import *
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'called', 'create_time', "is_site"]
    list_editable = ['called',]
    ordering = ['-create_time']
    list_filter = ['called',  'is_site']
    search_fields = ['tg_id', "course_1"]