from django.db import models
from patients.models import Paciente
from appointments.models import Citas


class Tratamiento(models.Model):
    cod_tratamiento = models.AutoField(db_column='Cod_Tratamiento', primary_key=True)
    descripcion = models.TextField(db_column='Descripcion')
    frecuencia = models.CharField(db_column='Frecuencia', max_length=7)
    tiempo_necesario = models.CharField(db_column='Tiempo_Necesario', max_length=20)
    num_serv_necesario = models.IntegerField(db_column='Num_Serv_Necesario')
    cod_paciente = models.ForeignKey(Paciente, models.CASCADE, db_column='Cod_Diagnostico')

    class Meta:
        managed = True
        db_table = 'tratamiento'

class Servicio(models.Model):
    cod_servicio = models.AutoField(db_column='Cod_Servicio', primary_key=True) 
    cod_cita = models.ForeignKey(Citas, models.CASCADE, db_column='Cod_Cita')
    precio = models.FloatField(db_column='Precio')
    tipo1 = models.CharField(db_column='Tipo1', max_length=20)
    tipo2 = models.CharField(db_column='Tipo2', max_length=20, blank=True, null=True)
    tipo3 = models.CharField(db_column='Tipo3', max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'servicio'
