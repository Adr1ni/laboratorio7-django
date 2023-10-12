from django import forms
from .models import Usuario, Evento, RegistroEvento

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'organizador']

class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = ['usuario', 'evento']
