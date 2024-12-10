from django.shortcuts import render,redirect
from .models import AsignacionFormulario, Respuesta

def realizar_formulario(request, asignacion_id):
    asignacion = AsignacionFormulario.objects.get(id=asignacion_id)
    if request.method == 'POST':
        for pregunta in asignacion.formulario.preguntas.all():
            respuesta_texto = request.POST.get(f'pregunta_{pregunta.id}')
            Respuesta.objects.create(asignacion=asignacion, pregunta=pregunta, respuesta_texto=respuesta_texto)
        return redirect('feedback')
    return render(request, 'realizar_formulario.html', {'asignacion': asignacion})
