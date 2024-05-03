from django.db import models

from django.contrib.auth.models import User

class Professor(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    position = models.CharField(max_length=50, verbose_name='Cargo')

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def __str__(self):
        return self.title + ' ' + self.full_name
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    enrollment = models.CharField(max_length=10, verbose_name='Matrícula')

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def __str__(self):
        return self.enrollment + " " + self.full_name

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'