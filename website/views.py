from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
import folium
#import geocoder
#from geopy.geocoders import Nominatim
from .models import Location


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
    #if (user) or (senha1!=senha2):
    if (user):
        return HttpResponse("Usuario já existe ou as senhas não são iguais")

    user = User.objects.create_user(username=email, password=senha1)
    user.save()
    return redirect('account')


#@login_required(login_url='/account/')
def profile(request):
    return render(request, "meuperfil.html")


#@login_required(login_url='/account/')
def maps(request):
    """
    — geolocator faz parte da funcionalidade que estava sendo desenvolvida
    — para quando nós tivessemos as coordenadas, fosse possivel conseguir a cidade
    — está parte do codigo ainda funciona, mas estava deixando o site muito lendo
    — para isso, decidi criar uma tabela no banco de dados com os campos city, lat e long
    — sendo assim, o site ficou bem mais leve
    — geolocator = Nominatim(user_agent="geoapiExercises")"""
    m = folium.Map(location=[-8.05950450471172, -34.88257613191841], zoom_start=10, width='100%', height='100%')

    locations = Location.objects.all()

    for local in locations:
        #loc = [float(local.lat), float(local.long)]
        loc = [local.lat, local.long]
        #location = geolocator.reverse(loc)
        #city = location.raw['address']['city']
        folium.Circle(loc, tooltip=local.city, fill_color='red').add_to(m)

    m = m._repr_html_()

    context = {
        'm': m,
    }
    return render(request, "maps.html", context)


def home(request):
    return render(request, "home.html")


def graficos(request):
    return render(request, "graficos.html")


def api(request):
    locations = Location.objects.all()
    context = {
        'locations': locations,
    }
    
    return render(request, 'api.html', context)