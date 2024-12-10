from django.db import models
from asignaciones.models import AsignacionFormulario
from form.models import Pregunta

class Respuesta(models.Model):
    asignacion = models.ForeignKey(AsignacionFormulario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_texto = models.TextField()

    def __str__(self):
        return f"Respuesta a {self.pregunta.texto} por {self.asignacion.usuario.username}"


