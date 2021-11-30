from django.urls import path
from django.urls.conf import include
from . import views



urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path("signup/", views.createUser, name="signup"),
    path("token/", views.token_send, name="token"),
    path("success/", views.success, name="success"),
    path("verify/<authentication_key>/", views.verify, name="verify"),
]