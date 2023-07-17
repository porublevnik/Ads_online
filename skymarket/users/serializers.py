from django.contrib.auth.hashers import make_password
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # def create(self, validated_data):
    #     validated_data['password'] = make_password(
    #         validated_data['password']
    #     )
    #     return User.objects.create(**validated_data)
    pass

class CurrentUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = User
        fields = '__all__'
