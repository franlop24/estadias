from django import forms

class EnrollmentForm(forms.Form):
    enrollment = forms.CharField(max_length=12, label = 'Matrícula', min_length=10)