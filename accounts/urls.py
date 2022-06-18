from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import RegisterAPIView, SendPasswordEmailApiView,ChangePasswordView, UserPasswordResetApiView
from django.urls import path, include

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register', RegisterAPIView.as_view()),
    path('resetpass', SendPasswordEmailApiView.as_view()),
    path('resetpass/<uid>/<token>', UserPasswordResetApiView.as_view()),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password')
]
