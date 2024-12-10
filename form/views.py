from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormularioForm, PreguntaForm
from .models import Formulario, Pregunta  # Importar el modelo

def form_index(request):
    # Recuperar todos los formularios
    formularios = Formulario.objects.all()
    return render(request, 'form/form_index.html', {'formularios': formularios})

def crear_formulario(request):
   # Crear un formulario con nombre y descripción
    if request.method == 'POST':
        if 'nombre' in request.POST and 'descripcion' in request.POST:
            # Crear el formulario (con nombre y descripción)
            formulario = Formulario(
                nombre=request.POST['nombre'],
                descripcion=request.POST['descripcion']
            )
            formulario.save()  # Guardar el formulario

            # Redirigir a la misma vista para agregar preguntas
            return redirect('crear_formulario')  # Recargar la página

        elif 'grupo_formulario' in request.POST and 'pregunta' in request.POST:
            # Agregar preguntas al formulario seleccionado
            grupo_formulario = Formulario.objects.get(id=request.POST['grupo_formulario'])
            pregunta_texto = request.POST['pregunta']
            tipo_respuesta = request.POST['tipo_respuesta']

            pregunta = Pregunta(
                texto=pregunta_texto,
                grupo=grupo_formulario,
                tipo_respuesta=tipo_respuesta
            )
            pregunta.save()  # Guardar la pregunta

            # Redirigir a la misma vista para seguir agregando preguntas
            return redirect('crear_formulario')  # Recargar la página

    # Recuperar todos los formularios creados para seleccionar uno
    formularios = Formulario.objects.all()

    # Filtrar las preguntas por el formulario seleccionado, si existe un formulario seleccionado
    formulario_id = request.GET.get('grupo_formulario', None)
    if formulario_id:
        preguntas = Pregunta.objects.filter(grupo_id=formulario_id)
    else:
        preguntas = Pregunta.objects.all()

    return render(request, 'form/crear_formulario.html', {'formularios': formularios,
        'preguntas': preguntas})



def listar_formularios(request):
    formularios = Formulario.objects.all()  # Obtener todos los formularios
    return render(request, 'form/listar_formularios.html', {'formularios': formularios})

def detalle_formulario(request, formulario_id):
    formulario = get_object_or_404(Formulario, id=formulario_id)
    return render(request, 'form/detalle_formulario.html', {'formulario': formulario})
