from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserPasswordResetSerializer, UserRegisterSerializers, SendPasswordEmailSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.permissions import IsAuthenticated   
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import ChangePasswordSerializer
# Create your views here.
class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializers
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            send_mail(
            'new subject', 
            f'hii', 
            'gurunathnandodkar@gmail.com', 
            [user.email], 
            fail_silently=False
        )
            serializer_data = {
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':serializer.data
            }
            return Response(serializer_data)
        return Response(serializer.errors)

class SendPasswordEmailApiView(APIView):
    serializer_class = SendPasswordEmailSerializer
    def post(self, request, format=None):
        serializer = SendPasswordEmailSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'msg':'Password reset link sent to your email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetApiView(APIView):
    serializer_class = UserPasswordResetSerializer
    def post(self, request, uid, token, formate=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        if serializer.is_valid():
            return Response({'msg':'Password reset successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





