from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register", views.UserRegisterView.as_view(), name="register"),
    path("login", views.UserLoginView.as_view(), name="login"),
    path('logout', views.UserLogoutView.as_view(next_page='/'), name='logout'),
    # path("profile", views.ProfileView.as_view(), name="profile"),
    # path("update-profile", views.update_profile, name="update_profile"),

]