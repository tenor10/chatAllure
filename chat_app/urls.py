from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("chat_page/<int:userid>", views.chat_page, name="chat_page"),
    path(
        "interlocutor_selection",
        views.interlocutor_selection,
        name="interlocutor_selection",
    ),
    path("message", views.message, name="message"),

]
