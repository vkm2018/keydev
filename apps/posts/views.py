from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.posts.models import Post, Rating, Comment
from apps.posts.serializers import PostSerializer, RatingSerializer, CommentSerializer


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        obj, _ = Rating.objects.get_or_create(post_id=pk, owner=request.user)
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj.rating = request.data['rating']
        obj.save()
        return Response(request.data, status=201)

    def get_permissions(self):

        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.rating =='rating':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]

        return [p() for p in permissions]

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

