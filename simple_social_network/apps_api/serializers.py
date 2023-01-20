from django.contrib.auth.models import User
from rest_framework import serializers

from app_posts.models import PhotoPost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoPost
        fields = '__all__'
