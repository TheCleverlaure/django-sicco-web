from django.db import models
from appointments.models import Citas
from payment.models import Pago

class CitaTienePago(models.Model):
    cod_cita = models.ForeignKey(Citas, models.CASCADE, db_column='Cod_Cita', primary_key=True)  # Field name made lowercase.
    cod_pago = models.ForeignKey(Pago, models.CASCADE, db_column='Cod_Pago', unique=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cita_tiene_pago'
        unique_together = (('cod_cita', 'cod_pago'),)
