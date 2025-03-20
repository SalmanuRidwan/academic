from django.contrib import admin
from .models import Task, Volunteer

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'status', 'report', 'assigned_volunteers_list')
    list_filter = ('status', 'location')
    search_fields = ('title', 'location', 'required_skills')
    filter_horizontal = ('assigned_volunteers',)
    ordering = ('status', 'title')

    def assigned_volunteers_list(self, obj):
        """Display assigned volunteers as a comma-separated list."""
        return ", ".join([str(volunteer) for volunteer in obj.assigned_volunteers.all()])
    assigned_volunteers_list.short_description = 'Assigned Volunteers'


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'is_available', 'skills')
    list_filter = ('is_available', 'location')
    search_fields = ('user__username', 'skills', 'location')
    ordering = ('user',)
