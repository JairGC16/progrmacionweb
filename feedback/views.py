from django.shortcuts import render
from asignaciones.models import AsignacionFormulario
from respuestas.models import Respuesta

def feedback_index(request):
    return render(request, 'feedback/feedback_index.html')

def feedback_index_user(request):
    return render(request, 'feedback/feedback_index_user.html')

# Create your views here.
def feedback(request, asignacion_id):
    asignacion = AsignacionFormulario.objects.get(id=asignacion_id)
    respuestas = Respuesta.objects.filter(asignacion=asignacion)
    recomendaciones = {}

    for respuesta in respuestas:
        # Puedes agregar aquí la lógica para generar recomendaciones
        recomendaciones[respuesta.pregunta.id] = f"Recomendación para: {respuesta.pregunta.texto}"

    return render(request, 'feedback.html', {'respuestas': respuestas, 'recomendaciones': recomendaciones})

