from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, required=True)
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)

    def validate(self, attrs):
        users = User.objects.filter(username=attrs.get('username'))
        emails = User.objects.filter(email=attrs.get('email'))

        if users.exists():
            raise serializers.ValidationError('Username already exist')

        if emails.exists():
            raise serializers.ValidationError('Email already exist')

        return attrs

    def save(self, **kwargs):
        username = self.validated_data.get('username')
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            is_active=True)
        Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, required=True)
    password = serializers.CharField(max_length=100, required=True)

    def validate(self, data):
        users = User.objects.filter(username=data.get('username'))
        if users.exists():
            user = users[0]
            Token.objects.get_or_create(user=user)
            is_valid_password = user.check_password(data.get('password'))

            if not is_valid_password:
                raise serializers.ValidationError('Invalid your password')

        else:
            raise serializers.ValidationError(f'{data.get("username")} not exist.')

        return data

    def get_dict(self):
        user = User.objects.get(username=self.validated_data.get('username'))
        token = Token.objects.get(user=user)

        return {
            'username': user.username,
            'token': token.key,
            'bearer': 'Token'
        }





