from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.posts.models import Post, Rating, Comment
from apps.posts.permissions import CustomIsAdmin
from apps.posts.serializers import PostSerializer, RatingSerializer, CommentSerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomIsAdmin]
    serializer_class = PostSerializer

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk)
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(request.data, status=201)


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

