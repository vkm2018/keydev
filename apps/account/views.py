from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.account.serializers import RegisterSerializer, LoginSerializer


# Create your views here.
class RegisterApiView(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = 'Вы успешно зарегистрировались.'

            return Response(message, status=200)


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer
