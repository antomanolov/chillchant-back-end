from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, DetailView
from app_profiles.appuser import AppUser
from django.contrib.auth.views import LoginView

from app_profiles.forms import CustomCreationFrom


class CreateUserView(CreateView):
    model = AppUser
    template_name = 'accounts/create_user.html'
    form_class = CustomCreationFrom
    success_url = 'accounts/create_user.html'

class SignUpView(LoginView):
    template_name = 'accounts/login.html'    
    next_page = reverse_lazy('index page')

class IndexView(ListView):
    model = AppUser
    template_name = 'accounts/index.html'

class UserDetailsView(DetailView):
    model = AppUser
    template_name = 'accounts/details.html'
