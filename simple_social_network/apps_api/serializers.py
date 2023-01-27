from django.contrib.auth.models import User
from rest_framework import serializers

from app_posts.models import PhotoPost, Comment, RatingPhoto, RatingComment, \
    Subscribe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoPost
        exclude = ('activity',)


class PostDetailAndAdd(serializers.ModelSerializer):
    class Meta:
        model = PhotoPost
        exclude = ('activity', 'likes', 'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('description',)


class RatingPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingPhoto
        fields = ('rating',)


class RatingCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingComment
        fields = ('rating',)


class SubscribeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'
