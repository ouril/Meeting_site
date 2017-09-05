from django.contrib import auth
from django.db.models import Q
from django.http import Http404
from django.shortcuts import (
    render,
    HttpResponseRedirect
)
from django.views.generic.detail import DetailView

from .models import UserAccount
from .forms import (
    RegForm,
    AccountForm,
    FindForm
)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(
            username=username,
            password=password
            )
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

    raise Http404


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/make_account')
        return render(request, 'registration.html', {'form': form})
    return render(request, 'registration.html', {'form': RegForm()})


def make_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'make_account.html', {'form': form})
    return render(request, 'make_account.html', {'form': AccountForm()})


def find_somebody(request):
    return render(request, 'index.html', {'form': FindForm()})


def filter(request):
    try:
        sex = request.POST.get('sex')
    except:
        sex = None
    try:
        age = request.POST.get('age')
    except:
        age = None
    if sex or age:
        context = UserAccount.objects.filter(
            Q(sex=sex)|
            Q(age=age)
        ).distinct()
    elif sex and age:
        context = UserAccount.objects.filter(
            Q(sex=sex)&
            Q(age=age)
        ).distinct()
    else:
        context = UserAccount.objects.all()
    return render(request, 'filter.html', {'account_list': context})


class UserAccountDetailView(DetailView):
    template_name = "detail.html"
    model = UserAccount
