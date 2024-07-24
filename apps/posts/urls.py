
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.posts.views import PostView, CommentView

router = DefaultRouter()
router.register('', PostView)
router.register(r'mark_add', CommentView)


urlpatterns=[

    path('', include(router.urls)),
]