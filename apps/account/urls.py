from django.contrib import admin
from django.urls import path

from apps.account.views import AccountView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', AccountView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', AccountView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ]