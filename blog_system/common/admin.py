from django.contrib import admin

from blog_system.common.models import BlogSystemSettings


class BlogSystemSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(BlogSystemSettings, BlogSystemSettingsAdmin)
