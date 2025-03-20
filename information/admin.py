from django.contrib import admin
from .models import Report, Tag

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'location', 'status', 'created_at', 'tags_list')  # Columns in list view
    list_filter = ('status', 'location', 'created_at')  # Sidebar filters
    search_fields = ('title', 'description', 'location', 'author__username')  # Searchable fields
    ordering = ('-created_at', 'status')  # Default ordering in admin view
    readonly_fields = ('created_at',)  # Make certain fields read-only

    def tags_list(self, obj):
        """Display tags as a comma-separated list."""
        return ", ".join([tag.name for tag in obj.tags.all()])
    tags_list.short_description = 'Tags'  # Column header name


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display tag names in list view
    search_fields = ('name',)  # Allow searching tags by name

