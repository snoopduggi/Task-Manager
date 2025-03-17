from django.urls import path
from .views import register_user, login_user, logout_user  # Import authentication views

urlpatterns = [
    path('register/', register_user, name='register_user'),  # API for User Registration
    path('login/', login_user, name='login_user'),  # API for Login
    path('logout/', logout_user, name='logout_user'),  # API for Logout
]
