from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class LoginUser(View):

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

