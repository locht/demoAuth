from django.urls import path
from account.api.views import RegistrationView

from rest_framework.authtoken import views

from rest_framework.authtoken.views import obtain_auth_token


app_name = 'account'

urlpatterns = [
    path('register', RegistrationView, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('view', views.obtain_auth_token, name='view_api'),
]