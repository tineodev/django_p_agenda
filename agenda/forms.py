from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido',required=False)
    telefono = forms.IntegerField(label='Telefono', required=True)