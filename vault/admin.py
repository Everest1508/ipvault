from django.contrib import admin
from .models import SSHConfig, AccessToken, FreeServer


class SSHConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port', 'username')
    search_fields = ('name', 'host', 'username')


admin.site.register(SSHConfig, SSHConfigAdmin)

# Register your models here.
admin.site.register(AccessToken)


@admin.register(FreeServer)
class FreeServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'api_link', 'renovation_date')
    search_fields = ('name', 'username', 'email', 'api_link')
    list_filter = ('renovation_date',)
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'username', 'email', 'password')
        }),
        ('API Details', {
            'fields': ('api_link', 'api_admin', 'api_password')
        }),
        ('Other Information', {
            'fields': ('renovation_date',)
        }),
    )
