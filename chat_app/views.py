import traceback
from django.shortcuts import render, redirect
from chat_app.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q



def index(request):
    return render(
        request,
        "index.html",
        {"user_list": User.objects.filter(is_active=True)},
    )


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request, "login.html", {"message": "Invalid username and/or password."}
            )
    else:
        return render(request, "login.html")


@login_required(login_url="login")
def message(request):
    id_user = request.POST.get("user_id")
    receiver = User.objects.get(pk=id_user)
    print(receiver)
    if request.method == "POST":
        message_send = request.POST["message"]
        try:
            new_message = Message(
                user=request.user, receiver=receiver, message=message_send
            )
            new_message.save()
            return chat_page(request, id_user)
        except Exception:
            traceback.print_exc()
            return chat_page(request, id_user)


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "register.html", {"message": "Passwords estão diferentes"}
            )
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "register.html", {"message": "Este usuário já existe"}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def interlocutor_selection(request):
    users = User.objects.filter(is_active=True)
    return render(
        request,
        "interlocutor_selection.html",
        {"user_list": users},
    )


def chat_page(request, userid):
    receiver = User.objects.get(pk=userid, is_active=True)
    messages = Message.objects.filter(
        Q(user=request.user, receiver=receiver) | Q(user=receiver, receiver=request.user))
    return render(
        request,
        "chat_page.html",
        {   
            "receiver": receiver,
            "messages": messages,
        },
    )

