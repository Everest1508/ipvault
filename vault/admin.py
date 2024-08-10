from django.contrib import admin
from .models import SSHConfig, AccessToken, FreeServer


class UserRestrictedAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers see all data
        return qs.filter(user=request.user)  # Non-superusers see only their data

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "user" and not request.user.is_superuser:
            kwargs["queryset"] = kwargs["queryset"].filter(id=request.user.id)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['user',]  # Make 'user' field readonly for non-superusers
        return super().get_readonly_fields(request, obj)


class SSHConfigAdmin(UserRestrictedAdmin):
    list_display = ('name', 'host', 'port', 'username')
    search_fields = ('name', 'host', 'username')


class AccessTokenAdmin(UserRestrictedAdmin):
    list_display = ('name', 'expires_in')
    search_fields = ('name',)


@admin.register(FreeServer)
class FreeServerAdmin(UserRestrictedAdmin):
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


# Register your models here.
admin.site.register(SSHConfig, SSHConfigAdmin)
admin.site.register(AccessToken, AccessTokenAdmin)
