from .forms import NewLoginForm, NewSignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from lab05_blog.models import Post

def signup(request):
    if request.method == "GET":
        form = NewSignupForm()
        return render(request, 'lab05_users/signup.html', {'form': form})
    elif request.method == "POST":
        form = NewSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            return HttpResponseRedirect(reverse('login'))

def user_login(request):
    if request.method == 'GET':
        return render(request, 'lab05_users/login.html', {'form': NewLoginForm()})
    elif request.method == "POST":
        form = NewLoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(request,username=form.cleaned_data['username'],password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                form.add_error('username', 'Invalid credentials')
                return render(request, 'lab05_users/login.html', {'form': form})

@login_required
def profile(request):
    posts = Post.objects.all().filter(user=request.user)
    return render(request, 'lab05_users/profile.html', {'lab05_blog': posts})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
