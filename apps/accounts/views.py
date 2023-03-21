from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm


# Create your views here.
class LoginUser(View):
    # A view that renders the login page and logs a user in
    def get(self, request):
        form = AuthenticationForm()
        context = {'form': form}
        template = 'accounts/login.html'
        return render(request, template, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            form = AuthenticationForm(
                data=request.POST,
            )
            context = {'form': form}
            return render(request, 'accounts/login.html', context)


class LogoutUser(View):
    # A view that logs a user out and redirects to the home page
    def get(self, request):
        logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('home')


class CreateUser(View):
    # A view that renders the register page and creates a new user
    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully ')

            return redirect('home')
        else:
            context = {'form': form}

            return render(request, 'accounts/register.html', context)

