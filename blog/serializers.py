from rest_framework import serializers
from django.core.validators import RegexValidator 
from .models import User

from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    mobile_number = serializers.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message='Mobile number must be 10 digits')]
    )
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email', 'mobile_number', 'password', 'gender']

    def create(self, validated_data):
        """
        No need to hash the password here as the User model's save method will handle it.
        This prevents double-hashing the password.
        """
        return User.objects.create(**validated_data)


