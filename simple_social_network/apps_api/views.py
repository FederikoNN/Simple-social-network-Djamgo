from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, \
    RetrieveModelMixin, DestroyModelMixin

from app_posts.models import PhotoPost
from apps_api.serializers import UserSerializer, PhotoSerializer


class UsersList(ListModelMixin, GenericAPIView):
    """Представление для получения списка постов и фильтрации по дате
    создания"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def get(self, request):
        return self.list(request)


class UserDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                 GenericAPIView):
    """Представление для получения детальной информации о пользователе, а также
    для его редактирования и удаления"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PhotoPostsList(ListModelMixin, GenericAPIView):
    """Представление для получения списка постов и фильтрации по дате
    создания"""
    queryset = PhotoPost.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_create']

    def get(self, request):
        return self.list(request)


class PhotoPostDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о посте, а также
    для его редактирования и удаления"""
    queryset = PhotoPost.objects.all()
    serializer_class = PhotoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

