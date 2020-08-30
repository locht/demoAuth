from django.urls import path
from account.api.views import RegistrationView #, CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'account'

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    # path('view', CustomAuthToken.as_view(), name='view_api')
]