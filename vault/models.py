# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class SSHConfig(models.Model):
    name = models.CharField(max_length=255, unique=True)
    host = models.GenericIPAddressField()
    port = models.PositiveIntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AccessToken(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    token = models.TextField(_("Access Token"))
    expires_in = models.DateField(_("Expires In"), auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.name