from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()

import uuid

class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    fullname = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("fullname", "email", "password", "password2")
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})

        validate_password(password)
        return data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        fullname = validated_data.get('fullname')

        # Generate username from email
        username = email.split('@')[0]

        # Check if username is available, if not, generate a unique username using uuid
        while User.objects.filter(username=username).exists():
            username = f"{username}_{str(uuid.uuid4())[:8]}"

        user = User.objects.create_user(username=username, email=email, password=password, full_name=fullname)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    gender = serializers.CharField(required=False)
    full_name = serializers.CharField(required=False)
    
    class Meta:
        model = User
        fields = ('id',"profile", 'full_name', 'email', 'date_of_birth','gender', 'mobile_number', "is_verified")