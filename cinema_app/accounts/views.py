from django.shortcuts import render

from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView, LogoutView

from cinema_app.accounts.forms import CustomUserCreationForm
from cinema_app.accounts.models import Customer
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate


class UserLogin(LoginView):
    next = 'home.html'

    # authentication_form
    # extra_content
    # redirect_authenticated_user
    # success_url_allowed_hosts
    # next
    # site
    # site_name

class UserRegister(FormView):
    template_name = 'registration/registration.html'

    form_class = CustomUserCreationForm

    def form_valid(self, form):
        # Add address and other info at ticket purchase
        user = form.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        login(self.request, user)

        return redirect('register-view')









