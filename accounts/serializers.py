from ast import Pass
from email.policy import default
from xml.dom import ValidationErr
from attr import attr
from click import style
from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserRegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password', 'password2']

    def create(self, validate_data):
        username = validate_data.get('username')
        email = validate_data.get('email')
        password = validate_data.get('password')
        password2 = validate_data.get('password2')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email allready exists")
        if password == password2:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return user


class SendPasswordEmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=120)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = 'http://127.0.0.1:8000/login/resetpass' + '/' + uid + '/' + token
            send_mail(
            'new subject', 
            f'password reset link is {link}', 
            'gurunathnandodkar@gmail.com', 
            [email], 
            fail_silently=False
            )
            return attrs
        else:
            raise ValidationErr('you are not registered user')



class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=120, style={'input_type':'password'}, write_only=True)
    password2 = serializers.CharField(max_length=120, style={'input_type':'password'}, write_only=True)
    class Meta:
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        uid = self.context.get('uid')
        token = self.context.get('token')
        if password != password2:
            raise serializers.ValidationError("password and confirm password dose not match")
        id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise ValidationErr('token is not valid')
        user.set_password(password)
        user.save()
        return attrs

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)















