from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.message import message
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_view(request):
    print(f"en register_view")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión después del registro
            return redirect("home")  # Redirigir a la página principal
        # else:
        #     for field, errors in form.errors.items():
        #         for error in errors:
        #             messages.error(request, error)
        else:
            error_messages = "\n".join(
                [" ".join(errors) for errors in form.errors.values()]
            )
            print(error_messages)
            msg = message("error", error_messages, 400)

            return render(
                request,
                "register.html",
                {"form": form, "message": json.dumps(msg.to_dict())},
            )
    else:
        form = CustomUserCreationForm()
        print(f"FORm2: {form}")
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserLoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)

    # Crear un mensaje de éxito con imagen
    msg = message(
        "info",
        "Se ha cerrado sesión exitosamente",
        200,
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8MIbugIhZBykSmQcR0QPcfnPUBOZQ6bm35w&s",
    )

    return render(request, "login.html", {"message": json.dumps(msg.to_dict())})


@login_required
def home_view(request):
    return render(request, "home.html")
