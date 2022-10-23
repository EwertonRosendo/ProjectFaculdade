from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required


# Create your views here.

def account(request):
    if(request.method=='GET'):
        return render(request, 'account.html')

    elif ((request.method) == "POST" and ("login" in request.POST)):
        login(request)

    elif ((request.method == "POST") and ("cadastro" in request.POST)):
        cadastro(request)
    else:
        return HttpResponse("DEU MERDA")


def login(request):
    email = request.POST.get("email_login")
    senha = request.POST.get("senha_login")

    user = authenticate(username=email, password=senha)

    if user:
        django_login(request, user)
        return redirect('profile')
    else:
        HttpResponse("EMAIL OU SENHA INVALIDOS")


def cadastro(request):
    email = request.POST.get('email_cadastro')
    senha1 = request.POST.get('password_cadastro1')
    senha2 = request.POST.get('password_cadastro2')

    user = User.objects.filter(username=email).first()
    if (user) or (senha1==senha2):
        return HttpResponse("Usuario já existe ou as senhas não são iguais")

    user = User.objects.create_user(username=email, password=senha1)
    user.save()
    return redirect('account')


#@login_required(login_url='/account/')
def profile(request):
    return render(request, "meuperfil.html")


#@login_required(login_url='/account/')
def maps(request):
    return render(request, "maps.html")


def blog(request):
    return render(request, "blog.html")


