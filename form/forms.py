from django import forms
from .models import Formulario, Pregunta

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre', 'descripcion']

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto', 'tipo_respuesta']