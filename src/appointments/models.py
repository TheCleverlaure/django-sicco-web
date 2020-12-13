from django.db import models
from date.models import Fecha
from patients.models import Paciente

class Citas(models.Model):
    cod_cita = models.AutoField(db_column='Cod_Cita', primary_key=True)
    hora = models.TimeField(db_column='Hora')
    precio = models.FloatField(db_column='Precio')
    asistencia = models.CharField(db_column='Asistencia', max_length=10, blank=True, null=True)
    cod_paciente = models.ForeignKey(Paciente, models.CASCADE, db_column='Cod_Paciente', blank=True, null=True)
    cod_fecha = models.ForeignKey(Fecha, models.CASCADE, db_column='Cod_Fecha', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'citas'

