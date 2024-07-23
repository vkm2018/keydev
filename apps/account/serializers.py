from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.account.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        if not User.objects.filter(username=username,).exist():
            raise serializers.ValidationError('Пользователь с таким username не существует')
        return username

    def validate(self, attrs):
        password = attrs.get('password')
        username = attrs.get('username')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError('Невервый пароль или username')
            attrs['user']=user
            return attrs