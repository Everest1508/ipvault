from rest_framework import serializers
from .models import SSHConfig, AccessToken

class SSHConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSHConfig
        fields = '__all__'

class AccessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessToken
        fields = '__all__'
