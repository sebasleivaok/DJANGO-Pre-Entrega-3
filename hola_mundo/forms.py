from django import forms

class PersonaForm(forms.Form):
    nombre = forms.Charfield(max_length=100)
    apellido = forms.Charfield(max_length=100)
    fecha_nacimiento = forms.DateField()
    