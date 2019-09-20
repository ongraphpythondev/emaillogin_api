from django.urls import path, include
from .views import UserCreate, Loginview


urlpatterns = [
    path("signup/", UserCreate.as_view(), name="user_create"),
    path("login/",Loginview.as_view(),name="login_view"),
    ]