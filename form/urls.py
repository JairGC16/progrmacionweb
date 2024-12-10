from django.urls import path
from . import views

urlpatterns = [
    path('form_index/', views.form_index, name='form_index'),
    path('crear/', views.crear_formulario, name='crear_formulario'),
    path('listar/', views.listar_formularios, name='listar_formularios'),
    path('detalle/<int:formulario_id>/', views.detalle_formulario, name='detalle_formulario'),  # Nueva ruta para ver detalles

]
