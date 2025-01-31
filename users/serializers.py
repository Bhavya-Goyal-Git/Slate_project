from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import StudentAchievement

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ["id", "email", "name", "password", "role"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
            role=validated_data["role"]
        )
        return user

class StudentAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAchievement
        fields = ["id", "name", "school_name", "achievements"]