from django.contrib import admin
from .models import Report, Media

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'status', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('report', 'file', 'uploaded_at')
    search_fields = ('report__title',)
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)

