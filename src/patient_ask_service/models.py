from django.db import models
from patients.models import Paciente
from treatment.models import Servicio


class PacienteSolicitaServicio(models.Model):
    cod_paciente = models.ForeignKey(Paciente, models.CASCADE, db_column='Cod_Paciente', primary_key=True)  # Field name made lowercase.
    cod_servicio = models.ForeignKey(Servicio, models.CASCADE, db_column='Cod_Servicio', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paciente_solicita_servicio'
        unique_together = (('cod_paciente', 'cod_servicio'),)
