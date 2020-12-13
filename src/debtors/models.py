from django.db import models
from patients.models import Paciente
from date.models import Fecha


class Moroso(Paciente):
    cod_moroso = models.AutoField(db_column='Cod_Moroso', primary_key=True)
    saldo_deudor = models.FloatField(db_column='Saldo_Deudor', blank=True, null=True)
    fecha_limite = models.DateField(db_column='Fecha_Limite', blank=True, null=True)
    fecha_ultimo_pago = models.DateField(db_column='Fecha_Ultimo_Pago', blank=True, null=True)
    cod_paciente_related = models.OneToOneField(Paciente, models.CASCADE, db_column='Cod_Paciente')
    cod_fecha = models.ForeignKey(Fecha, models.CASCADE, db_column='Cod_Fecha', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'moroso'
