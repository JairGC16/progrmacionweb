# surveys/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('formularios/', views.formulario_index, name='formulario_index'),
    path('formularios_user/', views.formulario_index_user, name='formulario_index_user'),
]
