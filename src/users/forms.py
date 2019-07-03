from django import forms
from src.users.models import DataUser

class UserForm(forms.ModelForm):
    class Meta:
        model = DataUser

        fields = [
            'userGender',
            'perfilPro', 
            'phone',
            'adress', 
        ]
        labels = {
            'userGender': 'Genero',
            'perfilPro': 'Tipo de perfil', 
            'phone': 'Telefono',
            'adress': 'Direccion', 
        }
        widgets = {
            'userGender': forms.TextInput(attrs= {'class': 'form-control'}),
            'perfilPro': forms.TextInput(attrs= {'class': 'form-control'}), 
            'phone': forms.TextInput(attrs= {'class': 'form-control'}),
            'adress': forms.TextInput(attrs= {'class': 'form-control'}), 
        }

