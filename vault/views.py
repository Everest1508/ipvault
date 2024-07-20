from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SSHConfig, AccessToken
from .serializers import SSHConfigSerializer, AccessTokenSerializer

class SSHConfigListView(generics.ListAPIView):
    queryset = SSHConfig.objects.all()
    serializer_class = SSHConfigSerializer
    permission_classes = [IsAuthenticated]

class AccessTokenListView(generics.ListAPIView):
    queryset = AccessToken.objects.all()
    serializer_class = AccessTokenSerializer
    permission_classes = [IsAuthenticated]
