# forms.py
from django import forms
from .models import Asignacion, Formulario, Pregunta
from django.contrib.auth.models import User

class AsignacionForm(forms.ModelForm):
    # Usamos el formulario para seleccionar un formulario y el usuario
    formulario = forms.ModelChoiceField(queryset=Formulario.objects.all(), required=True)
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    preguntas = forms.ModelMultipleChoiceField(queryset=Pregunta.objects.none(), required=True)

    class Meta:
        model = Asignacion
        fields = ['usuario', 'formulario', 'preguntas']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Inicializar las preguntas basadas en el formulario seleccionado
        if 'formulario' in self.data:
            formulario_id = self.data.get('formulario')
            self.fields['preguntas'].queryset = Pregunta.objects.filter(grupo_id=formulario_id)
        elif self.instance.pk:
            self.fields['preguntas'].queryset = self.instance.formulario.preguntas.all()

    def save(self, commit=True):
        asignacion = super().save(commit=False)
        asignacion.save()
        # Guardar las preguntas relacionadas
        self.cleaned_data['preguntas'].set(asignacion.preguntas.all())
        return asignacion
