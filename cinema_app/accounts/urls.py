

from django.urls import path

from cinema_app.accounts.views import UserLogin


urlpatterns = [
    path('login/', UserLogin.as_view, name='login-view'),
]