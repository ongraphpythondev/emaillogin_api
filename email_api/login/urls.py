from django.urls import path, include
from .views import UserCreate, Loginview, Logout
from rest_auth.views import LogoutView
urlpatterns = [
    path("signup/", UserCreate.as_view(), name="user_create"),
    path("login/",Loginview.as_view(),name="login_view"),

    path("logout/",LogoutView.as_view(),name="login_view"),
]