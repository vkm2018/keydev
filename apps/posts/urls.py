
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.posts.views import PostView, CommentView



urlpatterns=[

    path('', PostView.as_view()),
]