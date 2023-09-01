from django.urls import path

from app_common.views import like_view


urlpatterns = [
    path('like/<int:pk>', like_view, name='like'),
]
