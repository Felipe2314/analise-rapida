from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, WorkoutPlan, DietPlan


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "height",
            "weight",
            "goal",
            "created_at",
            "updated_at",
            "is_active",
        ]


class WorkoutPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = [
            "id",
            "user",
            "name",
            "description",
            "duration_weeks",
            "created_at",
            "updated_at",
            "is_active",
        ]


class DietPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = DietPlan
        fields = [
            "id",
            "user",
            "name",
            "calories_per_day",
            "notes",
            "created_at",
            "updated_at",
            "is_active",
        ]
