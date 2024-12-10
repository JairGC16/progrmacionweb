
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('home/', include('home.urls')), 
    path('formularios/', include('formularios.urls')),
    path('accounts/', include('accounts.urls')),
    path('form/', include('form.urls')),
    path('asignaciones/', include('asignaciones.urls')),
    path('respuestas/', include('respuestas.urls')),
    path('feedback/', include('feedback.urls')),
    path('', lambda _: redirect('accounts/logout')),  # Redirige a la ruta 'logout' sin namespace
]
