from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Modelo para las preguntas
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.question_text

# Modelo para las respuestas
class ResponseForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Relación con las preguntas
    answer = models.CharField(max_length=255)  # Aquí puedes cambiar el tipo dependiendo de las respuestas

    def __str__(self):
        return f"Respuesta de {self.user.username} a la pregunta: {self.question.question_text}"
