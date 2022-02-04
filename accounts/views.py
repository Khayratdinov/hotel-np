from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from accounts.forms import RegisterForm, UserUpdateForm
from accounts.models import CustomUser


# Create your views here.


# ---------------------------------------------------------------------------- #
#                                     USERS                                    #
# ---------------------------------------------------------------------------- #


def login_form(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.warning(request, 'Error Try Again Later')
            return redirect('login_form')

    return render(request, 'profile/login.html')


def register_user(request):
    success = False

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=password)

            user.save()
            messages.success(
                request, 'User created - please <a href="/login">login</a>.')
            success = True

            return redirect("login_form")

        else:
            messages.warning(request, "Registration error!")
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'success': success
    }

    return render(request, "profile/signup.html", context)


def logout_form(request):
    logout(request)
    return redirect('home')


# ---------------------------------------------------------------------------- #
#                                 USER PROFILE                                 #
# ---------------------------------------------------------------------------- #


def profile(request):

    return render(request, 'profile/profile.html')


def profile_edit(request, id):
    user = CustomUser.objects.get(id=id)
    form = UserUpdateForm(request.POST, request.FILES, instance=user)

    if form.is_valid():
        if request.FILES:
            user.avatar = request.FILES['avatar']
        form.save()
        return redirect('profile')

    form = UserUpdateForm(instance=user)
    return render(request, 'profile/profile_edit.html', {'user': user, 'form': form})
