from django.urls import path
from main.views import index, login, register, logout, about, profile


urlpatterns = [
    path("", index, name = "index"),
    path("logout", logout, name = "logout"),
    path("login", login, name = "login"),
    path("register", register, name = "register"),
    path("about/", about, name = "about"),
    path("profile/<str:username>", profile, name = "profile"), #profle/asliddin

]