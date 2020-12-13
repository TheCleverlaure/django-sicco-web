from django.db import models
from treatment.models import Servicio
from payment.models import Pago


class ServicioTienePago(models.Model):
    cod_servicio = models.ForeignKey(Servicio, models.CASCADE, db_column='Cod_Servicio', primary_key=True)  # Field name made lowercase.
    cod_pago = models.ForeignKey(Pago, models.CASCADE, db_column='Cod_Pago', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicio_tiene_pago'
        unique_together = (('cod_servicio', 'cod_pago'),)

