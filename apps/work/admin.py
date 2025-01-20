from django.contrib import admin
from .models import Work, ImageWork


class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'services', 'project']
    search_fields = ('services', 'project')
    list_filter = ('project', 'created_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Work, WorkAdmin)
admin.site.register(ImageWork)
