from django.contrib import admin
from .models import PhotoPost, Comment, RatingPhoto, Subscribe


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_create', 'user']


admin.site.register(PhotoPost, PostAdmin)
admin.site.register(Comment)
admin.site.register(RatingPhoto)
admin.site.register(Subscribe)
