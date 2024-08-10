from django.urls import path
from .views import SSHConfigListView, AccessTokenListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('ssh-configs/', SSHConfigListView.as_view(), name='ssh-config-list'),
    path('access-tokens/', AccessTokenListView.as_view(), name='access-token-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
