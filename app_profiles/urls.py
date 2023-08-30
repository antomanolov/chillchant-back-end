from django.urls import path

from app_profiles.views import CreateUserView, IndexView, SignUpView, UserDetailsView

urlpatterns = [
    path('',CreateUserView.as_view(), name='create user page'),
    path('login/', SignUpView.as_view(), name='login page'),
    path('index/', IndexView.as_view(), name='index page'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='details page')
]
