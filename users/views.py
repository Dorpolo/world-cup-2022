from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from enum import Enum

# Create your views here.
from .models import Profile
from .forms import CustomUserCreationForm


class ProfileBuilder:
    def __init__(self):
        self.context = {
            'data': {
                'some_data': 'some_data',
            }
        }
        self.template_name = 'users/profile_builder.html'

    # @login_required(login_url="login")
    def create(self, request) -> HttpResponse:
        form = ProfileForm()
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/leagues/fan-zone/')
        return render(
            request=request,
            template_name=self.template_name,
            context=dict(**self.context, form=form)
        )

    # @login_required(login_url="login")
    def update(self, request, pk) -> HttpResponse:
        prediction = LeagueMember.objects.get(id=pk)
        form = LeagueMemberForm(instance=prediction)
        if request.method == 'POST':
            form = LeagueMemberForm(request.POST, request.FILES, instance=prediction)
            if form.is_valid():
                form.save()
                return redirect('/leagues/fan-zone/')
        return render(
            request=request,
            template_name=self.template_name,
            context=dict(**self.context, form=form)
        )



class LoginPageType(Enum):
    LOGIN = 'login'
    LOGOUT = 'logout'
    REGISTER = 'register'



def doc(request) -> HttpResponse:
    return render(
        request=request,
        template_name='index0.html',
    )

def profiles(request) -> HttpResponse:
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(
        request=request,
        template_name='users/profiles.html',
        context=context
    )


def loginUser(request) -> HttpResponse:
    context = {
        'page': LoginPageType.LOGIN.value
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')
            return redirect('login')
    return render(
        request=request,
        template_name='users/login_register.html',
        context=context
    )


def logoutUser(request) -> HttpResponse:
    logout(request)
    return redirect('login')


def registerUser(request) -> HttpResponse:
    context = {
        'page': LoginPageType.REGISTER.value,
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Registeration has been failed.')

    return render(
        request=request,
        template_name='users/login_register.html',
        context=context
    )
