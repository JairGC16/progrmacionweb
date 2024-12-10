from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # La raíz ('') apunta a la vista home
    path('homeusuario/', views.homeuser, name='homeuser'),
    path('historial/', views.historial, name='historial'),
]