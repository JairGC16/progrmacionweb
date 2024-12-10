from django.contrib.auth.models import User
from django.db import models
from form.models import Formulario, Pregunta

class AsignacionFormulario(models.Model):
     # Relacionamos un formulario con un usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE)
    preguntas = models.ManyToManyField(Pregunta)  # Relación con preguntas asociadas al formulario

    fecha_asignacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.usuario.username} - {self.formulario.nombre}"
