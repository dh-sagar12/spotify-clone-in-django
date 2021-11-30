from django.urls import path
from . import views



urlpatterns = [
    path('@<str:username>/', views.showProfile, name='profile'),
    path('editprofile/', views.editProfile, name='editProfile'),
]