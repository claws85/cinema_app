

from django.urls import path

from cinema_app.accounts.views import UserLogin, UserRegister


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login-view'),
    path('register/', UserRegister.as_view(), name='register-view'),
]