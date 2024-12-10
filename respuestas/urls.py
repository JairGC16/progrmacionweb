from django.urls import path
from . import views

urlpatterns = [
    path('realizar/', views.realizar_formulario, name='realizar_formulario'),
]
