from django import forms
from .models import Contact, Atencion, Mecanico, Categoria, Postulacion

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class AtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = ["diagnostico","categoria","fecha_atencion","materiales","foto"]
        #fields = "__all__"

        widgets = {
            "fecha_atencion" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }

class ModificarAtencionForm(forms.ModelForm):
    class Meta:
        model = Atencion
        fields = "__all__"

        widgets = { 
            "fecha_atencion" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }


class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = ["nombre", "apellido", "rut", "edad", "fecha_nacimiento", "categoria", "foto", "usuario"]

        widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }

class ModificarMecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = "__all__"

        widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = "__all__"

        widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }