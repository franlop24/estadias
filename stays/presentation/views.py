from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages

from .forms import PresentationForm, FilterForm
from academy.models import Student
from .models import Presentation

def home(request, enrollment):
    student = Student.objects.get(enrollment=enrollment)
    user = student.user
    presentations = Presentation.objects.filter(student = student)
    if presentations:
        p = presentations[0]
    else:
        p = Presentation.objects.create(student = student)

    if request.method == 'POST':
        form = PresentationForm(request.POST)
        if form.is_valid():
            # Update Data User
            name_student = form.cleaned_data.get('name_student').upper()
            lastname_student = form.cleaned_data.get('lastname_student').upper()
            email_student = form.cleaned_data.get('email_student')
            user = student.user
            user.first_name = name_student
            user.last_name = lastname_student
            user.email = email_student
            user.save()
            # Update Data Presentation
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            career = form.cleaned_data.get('career')
            period = form.cleaned_data.get('period')
            group = form.cleaned_data.get('group')
            nss = form.cleaned_data.get('nss')
            payed = form.cleaned_data.get('payed')
            internal_advisor = form.cleaned_data.get('internal_advisor')

            p.address = address.upper()
            p.phone = phone
            p.career = career
            p.period = period.upper()
            p.group = group.upper()
            p.nss = nss.upper()
            p.payed = payed

            # Update Data Asesor Interno
            p.internal_advisor = internal_advisor

            # Update Data Empresa y Asesor Externo

            title_contact = form.cleaned_data.get('title_contact')
            full_name_contact = form.cleaned_data.get('full_name_contact')
            position_contact = form.cleaned_data.get('position_contact')
            
            p.title_contact = title_contact.upper()
            p.full_name_contact = full_name_contact.upper()
            p.position_contact = position_contact.upper()


            enterprice = form.cleaned_data.get('enterprice')
            in_catalog = form.cleaned_data.get('in_catalog')
            title_external = form.cleaned_data.get('title_external')
            full_name_external = form.cleaned_data.get('full_name_external')
            position_external = form.cleaned_data.get('position_external')
            p.enterprice = enterprice.upper()
            p.in_catalog = in_catalog
            p.title_external = title_external.upper()
            p.full_name_external = full_name_external.upper()
            p.position_external = position_external.upper()

            name_project = form.cleaned_data.get('name_project')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            period_stay = form.cleaned_data.get('period_stay')
            register_date = form.cleaned_data.get('register_date')
            modality = form.cleaned_data.get('modality')
            line = form.cleaned_data.get('line')
            p.name_project = name_project.upper()
            p.start_date = start_date
            p.end_date = end_date
            p.period_stay = period_stay.upper()
            p.register_date = register_date
            p.modality = modality.upper()
            p.line = line.upper()
            p.save()
            messages.success(request, "Información Actualizada")
            return render(request, 'presentation/home.html', {'enrollment': enrollment, "form": form})

    form = PresentationForm()
    form.fields['name_student'].initial = student.user.first_name
    form.fields['lastname_student'].initial = student.user.last_name
    form.fields['email_student'].initial = student.user.email

    form.fields['address'].initial = p.address
    form.fields['phone'].initial = p.phone
    form.fields['career'].initial = p.career
    form.fields['period'].initial = p.period
    form.fields['group'].initial = p.group
    form.fields['nss'].initial = p.nss
    form.fields['payed'].initial = p.payed
    form.fields['internal_advisor'].initial = p.internal_advisor
    form.fields['title_contact'].initial = p.title_contact
    form.fields['full_name_contact'].initial = p.full_name_contact
    form.fields['position_contact'].initial = p.position_contact
    form.fields['enterprice'].initial = p.enterprice
    form.fields['in_catalog'].initial = p.in_catalog
    form.fields['title_external'].initial = p.title_external
    form.fields['full_name_external'].initial = p.full_name_external
    form.fields['position_external'].initial = p.position_external
    form.fields['name_project'].initial = p.name_project
    form.fields['start_date'].initial = p.start_date.strftime('%Y-%m-%d')
    form.fields['end_date'].initial = p.end_date.strftime('%Y-%m-%d')
    # print(p.end_date.strftime('%Y-%m-%d'))
    form.fields['period_stay'].initial = p.period_stay
    form.fields['register_date'].initial = p.register_date.strftime('%Y-%m-%d')
    form.fields['modality'].initial = p.modality
    form.fields['line'].initial = p.line

    return render(request, 'presentation/home.html', {'enrollment': enrollment, "form": form})

def presentation_list(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)

        if form.is_valid():
            career = form.cleaned_data.get('career')
            professor = form.cleaned_data.get('professor')
            
            if career and professor:
                presentations = Presentation.objects.filter(internal_advisor=professor, career = career)
            elif career:
                presentations = Presentation.objects.filter(career = career)
            elif professor:
                presentations = Presentation.objects.filter(internal_advisor=professor)
            else:
                presentations = Presentation.objects.all()

            return render(request, 'presentation/list.html', {"presentations": presentations, "form": form})        

    form = FilterForm()
    presentations = Presentation.objects.all()
    return render(request, 'presentation/list.html', {"presentations": presentations, "form": form})