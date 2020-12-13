from django.db import models

class Fecha(models.Model):
    cod_fecha = models.AutoField(db_column='Cod_Fecha', primary_key=True)
    fecha_f = models.DateField(db_column='Fecha_F')

    class Meta:
        managed = True
        db_table = 'fecha'

