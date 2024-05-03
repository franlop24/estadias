from django.db import models

from academy.models import Professor, Student
from career.models import Career
from django.utils import timezone

class Presentation(models.Model):
    #Datos del estudiante
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name='Estudiante')
    address = models.CharField(max_length=250, verbose_name='Dirección', default='')
    phone = models.CharField(max_length=10, verbose_name='Teléfono', default='0000000000')
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name='Carrera', null=True)
    period = models.CharField(max_length=20, verbose_name='Cuatrimestre', default='6')
    group = models.CharField(max_length=2, verbose_name='Grupo', default='A')
    nss = models.CharField(max_length=20, verbose_name='Número de Seguridad Social', default='000000000')
    payed = models.CharField(max_length=20, verbose_name='Pagado Hasta', default='6')

    #Datos del asesor interno
    internal_advisor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Asesor Interno', null=True)

    #Datos del empresa Contacto
    title_contact = models.CharField(max_length=20, verbose_name='Título', default='LIC')
    full_name_contact = models.CharField(max_length=100, verbose_name='Nombre Completo', default='')
    position_contact = models.CharField(max_length=150, verbose_name='Cargo', default='DIRECTOR')
    enterprice = models.CharField(max_length=150, verbose_name='Empresa', default='ACME AC')
    in_catalog = models.BooleanField(default=False, verbose_name='Empresa en Catálogo')

    #datos del asesor externo
    title_external = models.CharField(max_length=20, verbose_name='Título de Asesor Externo', default='LIC')
    full_name_external = models.CharField(max_length=100, verbose_name='Nombre Asesor Externo', default='')
    position_external = models.CharField(max_length=150, verbose_name='Cargo de Asesor Externo', default='DIRECTOR')

    # Datos del proyecto
    name_project = models.CharField(max_length=150, verbose_name='Nombre del Proyecto', default='')
    start_date = models.DateField(verbose_name='Fecha de Inicio', default=timezone.now)
    end_date = models.DateField(verbose_name='Fecha de Fin', default=timezone.now)
    period_stay = models.CharField(max_length=50, verbose_name='Periodo de Estancia', default='MAYO - AGOSTO')
    register_date = models.DateField(verbose_name='Fecha de Registro', default=timezone.now)
    modality = models.CharField(max_length=150, verbose_name='Modalidad', default='PRESENCIAL')
    line = models.CharField(max_length=150, verbose_name='Giro', default='EDUCACIÓN')

    def __str__(self):
        return self.student.enrollment + " " + self.student.full_name