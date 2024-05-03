from django.forms import ModelForm

from academy.models import Professor

from .models import Presentation
from django import forms

from career.models import Career

class PresentationForm(ModelForm, forms.Form):
    # enrollment = forms.CharField(max_length=100, label='Matrícula')
    name_student = forms.CharField(max_length=100, label='Nombre')
    lastname_student = forms.CharField(max_length=100, label='Apellidos')
    email_student = forms.EmailField(label='Correo')
    class Meta:
        model = Presentation
        fields = ["address", "phone", "career", "period", "group", "nss", "payed", "internal_advisor",
"title_contact", "full_name_contact", "position_contact", "enterprice", "in_catalog", "title_external", "full_name_external", 
"position_external", "name_project", "start_date", "end_date", "period_stay", "register_date", "modality", "line"]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'register_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FilterForm(forms.Form):
    career = forms.ModelChoiceField(queryset=Career.objects.all(), label='Carrera', required=False)
    professor = forms.ModelChoiceField(queryset=Professor.objects.all(), label='Asesor Interno', required=False)