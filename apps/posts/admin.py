from django.contrib import admin

from apps.posts.models import Post, Rating, Comment

# Register your models here.
admin.site.register(Post),
admin.site.register(Rating),
admin.site.register(Comment)
