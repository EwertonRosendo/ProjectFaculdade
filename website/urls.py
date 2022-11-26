from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'), 
    path('maps/', views.maps, name='blog' ),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('graficos/', views.graficos, name='graficos'),
    path('api/', views.api, name='api'),
    path('api/edit/<int:location_pk>', views.location_edit, name='edit_location')
    
]
