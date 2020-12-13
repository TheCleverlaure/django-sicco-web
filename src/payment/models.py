from django.db import models
from patients.models import Paciente
from date.models import Fecha
from debtors.models import Moroso


class Pago(models.Model):
    cod_pago = models.AutoField(db_column='Cod_Pago', primary_key=True)
    monto = models.FloatField(db_column='Monto')
    inicial = models.FloatField(db_column='Inicial', blank=True, null=True)
    cuota1 = models.FloatField(db_column='Cuota1', blank=True, null=True)
    cuota2 = models.FloatField(db_column='Cuota2', blank=True, null=True)
    tipo_pago = models.CharField(db_column='Tipo_Pago', max_length=8)
    metodo_pago = models.CharField(db_column='Metodo_Pago', max_length=10)
    num_ref = models.IntegerField(db_column='Num_Ref', blank=True, null=True)
    cod_fecha = models.ForeignKey(Fecha, models.CASCADE, db_column='Cod_Fecha', blank=True, null=True)
    cod_paciente = models.ForeignKey(Paciente, models.CASCADE, related_name='cod_paciente_link', db_column='Cod_Paciente', blank=True, null=True)
    cod_moroso = models.ForeignKey(Moroso, models.CASCADE, related_name='cod_moroso_link', db_column='Cod_Moroso', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pago'


class Recibo(models.Model):
    cod_recibo = models.AutoField(db_column='Cod_Recibo', primary_key=True)
    num_pago = models.IntegerField(db_column='Num_Pago', blank=True, null=True)
    cod_paciente = models.ForeignKey(Paciente, models.CASCADE, db_column='Cod_Paciente')
    cod_pago = models.ForeignKey(Pago, models.CASCADE, db_column='Cod_Pago', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recibo'

