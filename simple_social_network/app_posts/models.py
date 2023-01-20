from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class PhotoPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='название фото')
    description = models.CharField(max_length=100,
                                   verbose_name='подпись к фото')
    date_create = models.DateField(auto_now_add=True,
                                   verbose_name='дата публикации')
    activity = models.IntegerField(default=0,
                                   verbose_name='количество комментариев')
    likes = models.IntegerField(default=0, verbose_name='количество лайков')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Comment(models.Model):
    description = models.CharField(max_length=10000,
                                   verbose_name='текст комментария')
    post_comment = models.ForeignKey('PhotoPost', on_delete=models.CASCADE,
                                     related_name='post',
                                     verbose_name='Новость')
    likes = models.IntegerField(default=0, verbose_name='количество лайков')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class LikePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey('PhotoPost', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'photo')
        verbose_name = 'Нравится'


class LikeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'comment')
        verbose_name = 'Нравится'


class Subscribe(models.Model):
    user_follower = models.ForeignKey(User, related_name='followers',
                                      on_delete=models.CASCADE)
    user_following = models.ForeignKey(User, related_name='following',
                                       on_delete=models.CASCADE)
