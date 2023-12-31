from django.urls import path

from app_profiles.views import CreateUserView, IndexView, SignOutView, SignUpView, UserDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='index page'),
    path('create-user/',CreateUserView.as_view(), name='create user page'),
    path('login/', SignUpView.as_view(), name='login page'),
    path('logout/', SignOutView.as_view(), name='logout page'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='details page'),
]
