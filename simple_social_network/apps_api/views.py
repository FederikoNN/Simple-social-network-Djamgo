from django.db.models import Avg
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, \
    RetrieveUpdateDestroyAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .permissions import IsPhotoPostOwnerOrReadOnly
from apps_api.serializers import *


class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class PhotoPostsList(ListAPIView):
    queryset = PhotoPost.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)


class PhotoPostCreate(ListCreateAPIView):
    queryset = PhotoPost.objects.all()
    serializer_class = PostDetailAndAdd
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoPostDetail(RetrieveUpdateDestroyAPIView):
    queryset = PhotoPost.objects.all()
    serializer_class = PostDetailAndAdd
    permission_classes = (IsPhotoPostOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentsToPhotoPost(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = Comment.objects.filter(post_comment_id__id=post_id)
        return queryset


class CommentAddToPhotoPost(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentAddSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        serializer.save(user=self.request.user, post_comment_id=post_id)


class RatingAddPhotoPost(APIView):
    serializer_class = RatingPhotoSerializers
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        post_instance = get_object_or_404(PhotoPost, pk=kwargs['pk'])
        rating_instance, created = RatingPhoto.objects.get_or_create(
            user=request.user, photo=post_instance,
            defaults={'rating': int(request.POST.get('rating'))})
        if created:
            response = {'message': 'Accepted'}
        else:
            response = {'message': 'Not Accepted- Already rated'}
        rating_instance.save()
        post_instance.rating = post_instance.ratingphoto_set.all().aggregate(
            Avg('rating')).get('rating__avg')
        post_instance.save()
        return JsonResponse(response)


class RatingAddComment(APIView):
    serializer_class = RatingCommentSerializers
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        comment_instance = get_object_or_404(Comment, id=kwargs['sk'])
        rating_instance, created = RatingComment.objects.get_or_create(
            user=request.user, comment=comment_instance,
            defaults={'rating': int(request.POST.get('rating'))})
        if created:
            response = {'message': 'Accepted'}
        else:
            response = {'message': 'Not Accepted- Already rated'}
        rating_instance.save()
        comment_instance.rating = comment_instance.ratingcomment_set.all(

        ).aggregate(
            Avg('rating')).get('rating__avg')
        comment_instance.save()
        return JsonResponse(response)


class PhotoPostTop10(ListAPIView):
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = PhotoPost.objects.order_by('-rating')[:10]
        return queryset


class SubscribesUser(ListAPIView):
    queryset = PhotoPost.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.queryset, self.request.user)
        return super().get_queryset().filter(
            user__following__user_follower=self.request.user)


class SubscribeAdd(ListCreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializers
    permission_classes = (IsAuthenticated,)
