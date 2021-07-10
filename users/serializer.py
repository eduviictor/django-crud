from rest_framework import serializers, validators
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'lastName', 'profileImageUrl', 'bio', 'email', 'gender']