# Generated by Django 5.0.4 on 2024-05-02 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
        ('career', '0001_initial'),
        ('presentation', '0002_presentation_enterprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='career',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='internal_advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.professor', verbose_name='Asesor Interno'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='period',
            field=models.CharField(default='6', max_length=20, verbose_name='Cuatrimestre'),
        ),
    ]