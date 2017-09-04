from django.contrib import auth
from django.http import Http404
from django.shortcuts import (
    render,
    HttpResponseRedirect
)

from .forms import RegForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(
            username = username,
            password = password
            )
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/products')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'registration.html', {'form': form})
    return render(request, 'registration.html', {'form': RegForm()})