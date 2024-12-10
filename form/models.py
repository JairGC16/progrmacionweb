from django.db import models

class Formulario(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    TIPO_RESPUESTA = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Sí/No'),
    ]
    
    grupo = models.ForeignKey(Formulario, related_name='preguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    tipo_respuesta = models.CharField(max_length=8, choices=TIPO_RESPUESTA)

    def __str__(self):
        return self.texto
