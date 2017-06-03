from django.shortcuts import render
from django.utils import timezone
from django import forms
#회원가입
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm, MacForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.template import Context
from django.template.loader import get_template
from .models import Test


def main_index(request):
    return render(request, 'Main/index.html', {})

def signup(request):
    """signsup
    to register users
    """
    if request.method == "POST":
        userform = RegisterForm(request.POST)
        if userform.is_valid():
            new_user = User.objects.create_user(**userform.cleaned_data)
            return render(request, "registration/signup_ok.html", {"userform": userform,})

    elif request.method =="GET":
        userform = RegisterForm()

    return render(request, "registration/signup.html", {"userform": userform,})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'registration/signup_ok.html', {'form': form})


def signup_ok(request):
    if request.method == "POST":
        form = MacForm(request.POST)
        if form.is_valid():
            form.id = request.id
            form.save()
            return render(request,'main/index.html', {"form": form})
    else:
        form= MacForm()
    return render(request,  'registration/signup_ok.html', {"form": form})

def record(request):
    test = Test.objects.all()
    return render(request, 'fire/record.html',  {'test': test})
