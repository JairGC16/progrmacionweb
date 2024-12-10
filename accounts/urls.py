from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),      # URL para registro de usuarios
    path('login/', views.login_view, name='login'),          # URL para login
    path('logout/', views.logout_view, name='logout'),       # URL para logout
    path('users/', views.user_list, name='user_list'),       # URL para la lista de usuarios
    path('users/<int:id>/edit/', views.user_update, name='user_update'),   # URL para editar usuario
    path('users/<int:id>/delete/', views.user_delete, name='user_delete'), # URL para eliminar usuario
]
