from django.shortcuts import render, redirect
from .models import Formulario, AsignacionFormulario

def asignaciones_index(request):
    return render(request, 'asignaciones/asignaciones_index.html')



def asignar_formulario(request, formulario_id):
    formulario = Formulario.objects.get(id=formulario_id)
    if request.method == 'POST':
        usuarios = User.objects.all()  # O elegir un usuario específico
        for usuario in usuarios:
            AsignacionFormulario.objects.create(usuario=usuario, formulario=formulario)
        return redirect('asignar_formulario')
    return render(request, 'asignacion_form.html', {'formulario': formulario})
