
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.posts.views import PostView, CommentView

router = DefaultRouter()
router.register('', PostView)
router.register('comment', CommentView)


urlpatterns=[

    path('', include(router.urls)),
]