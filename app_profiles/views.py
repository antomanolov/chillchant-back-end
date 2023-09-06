from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, DetailView
from app_profiles.appuser import AppUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from app_profiles.forms import CustomCreationFrom


class CreateUserView(CreateView):
    model = AppUser
    template_name = 'accounts/create_user.html'
    form_class = CustomCreationFrom
    success_url = 'index page'

class SignUpView(LoginView):
    template_name = 'accounts/login.html'    
    next_page = reverse_lazy('index page')

class SignOutView(LogoutView):
    next_page = reverse_lazy('index page')

class IndexView(ListView):
    model = AppUser
    template_name = 'common/index.html'
    
    

class UserDetailsView(DetailView):
    model = AppUser
    template_name = 'accounts/details.html'
