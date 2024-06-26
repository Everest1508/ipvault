from django.contrib import admin
from .models import SSHConfig,AccessToken

class SSHConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'host', 'port', 'username')
    search_fields = ('name', 'host', 'username')

admin.site.register(SSHConfig, SSHConfigAdmin)

# Register your models here.
admin.site.register(AccessToken)