from django.contrib import admin
from .models import Contact, ContactMe


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'is_published']
    list_filter = ('full_name', 'phone_number', 'is_published')
    search_fields = ('full_name', 'phone_number')
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactMe)
