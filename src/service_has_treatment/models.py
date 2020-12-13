from django.db import models
from treatment.models import Servicio, Tratamiento


class ServicioTieneTratamiento(models.Model):
    cod_servicio = models.ForeignKey(Servicio, models.CASCADE, db_column='Cod_Servicio', primary_key=True)
    cod_tratamiento = models.ForeignKey(Tratamiento, models.CASCADE, db_column='Cod_Tratamiento', unique=True)

    class Meta:
        managed = False
        db_table = 'servicio_tiene_tratamiento'
        unique_together = (('cod_servicio', 'cod_tratamiento'),)

