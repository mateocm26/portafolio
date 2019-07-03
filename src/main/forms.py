from django import forms
from src.main.models import *

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education

        fields = [
            'institute',
            'title', 
            'date',
        ]
        labels = {

            'institute': 'Institucion',
            'title': 'Titulo', 
            'date': 'Fecha',
            
        }
        widgets = {
            'institute': forms.TextInput(attrs= {'class': 'form-control'}),
            'title': forms.TextInput(attrs= {'class': 'form-control'}), 
            'date': forms.TextInput(attrs= {'class': 'form-control'}),
        }

class AbilitiesForm(forms.ModelForm):
    class Meta:
        model = Abilities

        fields = [
            'abilitieName',
            'abilitieLevel', 
        ]
        labels = {

            'abilitieName': 'Habilidades',
            'abilitieLevel': 'Nivel de la habilidad', 
            
        }
        widgets = {
            'abilitieName': forms.TextInput(attrs= {'class': 'form-control'}),
            'abilitieLevel': forms.TextInput(attrs= {'class': 'form-control'}), 
        }
