from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.models import User
from apps.account.serializers import RegisterSerializer, LoginSerializer, AccountSerializer


# Create your views here.
class AccountView(APIView):

    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = 'Вы успешно зарегистрировались.'

            return Response(message, status=200)

    def get(self, request):
        users = User.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data, status=200)





class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer
