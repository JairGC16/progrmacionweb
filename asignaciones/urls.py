from django.urls import path
from . import views

urlpatterns = [
    path('asignar/', views.asignaciones_index, name='asignaciones_index'),
]

