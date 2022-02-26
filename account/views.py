# from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(form.cleaned_data)
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})
