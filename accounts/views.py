from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from .forms import *


def index(request):
    return render(request, 'accounts/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and user.is_superadmin:

                login(request, user)
                return redirect('siteadmin:index')
            elif user.is_active and user.is_poolhost:

                login(request, user)
                return redirect('poolhost:index')
            elif user.is_active and user.is_pooluser:

                login(request, user)
                return redirect('pooluser:index')
            else:
                print('user is not active')
                return HttpResponse("error")
        else:
            return HttpResponse("error")
    else:
        return render(request, "accounts/login.html")


def superuser_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superadmin = True
            user.set_password(request.POST.get('password'))
            user.save()
            return redirect('accounts:user_login')
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/user_register.html', {'form': form})
