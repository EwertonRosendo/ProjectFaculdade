from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
import folium
#import geocoder
#from geopy.geocoders import Nominatim
from .models import Location
from .forms import LocationForm


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

    if request.POST:
        form = LocationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('api')
    form = LocationForm()
    context = {
        'm': m,
        'form': form
    }
    return render(request, "maps.html", context)


def home(request):
    locations = Location.objects.all()
    context = {
        'locations': locations
    }
    return render(request, "home.html", context)


def graficos(request):
    return render(request, "graficos.html")


def api(request):
    locations_list = Location.objects.all()
    paginator = Paginator(locations_list, 10)  # Mostra 10 localizações por página

    # Make sure page request is an int. If not, deliver first page.
    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        locations = paginator.page(page)
    except (EmptyPage, InvalidPage):
        locations = paginator.page(paginator.num_pages)

    return render(request, 'api.html', {"locations": locations})


def location_edit(request, location_pk):

    location = Location.objects.get(pk=location_pk)
    form = LocationForm(request.POST, instance=location)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('api')
    context = {
        'form': form,
        'location': location_pk
    }
    return render(request, 'edit.html', context=context)


""" 
A função location_delete é usada para deletar localizações.
A função recebe um parametro que é a chave primaria do local que será
deletado e o usa como argumento para chamar a função de deletar
"""
def location_delete(request, location_pk):

    location = Location.objects.get(pk=location_pk)
    location.delete()

    return redirect('api')

def post(request):
    return render(request, 'post.html')