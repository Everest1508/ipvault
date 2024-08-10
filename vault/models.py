# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class SSHConfig(models.Model):
    name = models.CharField(max_length=255, unique=True)
    host = models.GenericIPAddressField()
    port = models.PositiveIntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.ManyToManyField(
        User, related_name='ssh_configs')

    def __str__(self):
        return self.name


class AccessToken(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    token = models.TextField(_("Access Token"))
    expires_in = models.DateField(
        _("Expires In"), auto_now=False, auto_now_add=False)

    user = models.ManyToManyField(
        User, related_name='access_token')

    def __str__(self) -> str:
        return self.name


class FreeServer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    username = models.CharField(_("Username"), max_length=250)
    email = models.EmailField(_("Email"), max_length=254)
    password = models.CharField(_("Password"), max_length=255)
    api_link = models.URLField(_("API URL"), max_length=500)
    api_admin = models.CharField(_("Admin Username"), max_length=400)
    api_password = models.CharField(_("Admin Password"), max_length=400)
    renovation_date = models.DateField(
        _("Renovation Field"), auto_now=False, auto_now_add=False, null=True, blank=True)
    user = models.ManyToManyField(
        User, related_name='free_server')
