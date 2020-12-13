from django.db import models
from persona.models import Persona

class Paciente(Persona):
    cod_paciente = models.AutoField(db_column='Cod_Paciente', primary_key=True)
    diagnostico = models.TextField(db_column='Diagnostico')
    ci_related = models.OneToOneField(Persona, models.CASCADE, db_column='CI')

    class Meta:
        managed = True
        db_table = 'paciente'


class Expediente(models.Model):
    cod_expediente = models.AutoField(db_column='Cod_Expediente', primary_key=True)
    antecedentes_clinicos = models.TextField(db_column='Antecedentes_Clinicos', blank=True, null=True)
    enfermedades = models.CharField(db_column='Enfermedades', max_length=50, blank=True, null=True)
    alergias = models.CharField(db_column='Alergias', max_length=50, blank=True, null=True)
    cod_paciente = models.OneToOneField(Paciente, models.CASCADE, db_column='Cod_Paciente')

    class Meta:
        managed = True
        db_table = 'expediente'

