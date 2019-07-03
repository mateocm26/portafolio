from django import forms

from src.main.models import *

class MainForm(forms.ModelForm):
    class Meta:
        model = Education

        fields = [
            'institute',
            'title',
            'date'
        ]

        labels = {
            'institute': 'Institute',
            'title' : 'Title',
            'date' : 'Date',
        }