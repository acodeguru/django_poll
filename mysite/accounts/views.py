"""
Account view - SignUp/SignIn & Logout operations
"""
import logging as logger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm


def signin(request):
    """
    Sign in operation of user
    """
    if request.user.is_authenticated:
        return redirect('polls:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            logger.info("%s is logged in", username)
            redirect_url = request.GET.get('next', 'polls:index')
            return redirect(redirect_url)

        messages.error(request, "Username Or Password is incorrect!!",
                       extra_tags='alert alert-danger alert-dismissible fade show')

    return render(request, 'accounts/signin.html')


def user_logout(request):
    """
    logout operation of user
    """
    logout(request)
    return redirect('accounts:signin')


def signup(request):
    """
    Sign up operation of user
    """
    if request.user.is_authenticated:
        return redirect('polls:index')

    if request.method == 'POST':
        errors = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            email = form.cleaned_data['email']

            if password != password_confirm:
                errors = True
                messages.error(request, 'Password doesn\'t matched',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                errors = True
                messages.error(request, 'Username already exists',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                errors = True
                messages.error(request, 'Email already registered',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if errors:
                messages.error(
                    request,
                    "Registration Failed",
                    extra_tags='alert alert-warning alert-dismissible fade show'
                )
                return redirect('accounts:signup')

            user = User.objects.create_user(
                username=username, password=password, email=email)
            logger.info("new user created successfully %s", user.username)
            messages.success(
                request, f'Thanks for registering {user.username}!',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('accounts:signin')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/signup.html', {'form': form})
