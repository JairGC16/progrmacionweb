from django.shortcuts import render

# Create your views here.
# surveys/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, ResponseForm
from django.contrib.auth.decorators import login_required

# Vista para ver las preguntas y responderlas
# @login_required

def formulario_index(request):
    return render(request, "formularios/formulario_index.html")

def formulario_index_user(request):
    return render(request, "formularios/formulario_index_user.html")

def formulario_view(request):
    questions = Question.objects.all()  # Obtener todas las preguntas
    
    if request.method == "POST":
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer:
                ResponseForm.objects.create(user=request.user, question=question, answer=answer)
        return HttpResponse("Gracias por responder las preguntas.")
    
    return render(request, "formularios/formulario.html", {"questions": questions})
