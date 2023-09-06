from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, DetailView
from app_profiles.appuser import AppUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from app_profiles.forms import CustomAuthForm, CustomCreationFrom

# TODO view how to implement error msgs in the Login Form!
class CreateUserView(CreateView):
    model = AppUser
    template_name = 'accounts/create_user.html'
    form_class = CustomCreationFrom
    success_url = 'index page'

class SignUpView(LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthForm    
    next_page = reverse_lazy('index page')

class SignOutView(LogoutView):
    next_page = reverse_lazy('index page')

class IndexView(LoginRequiredMixin, ListView):
    model = AppUser
    template_name = 'common/index.html'
    login_url = 'login page'
    
    

class UserDetailsView(DetailView):
    model = AppUser
    template_name = 'accounts/details.html'
