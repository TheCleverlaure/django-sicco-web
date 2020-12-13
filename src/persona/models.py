from django.db import models

class Persona(models.Model):
    ci = models.CharField(db_column='CI', primary_key=True, max_length=10)
    nombre = models.CharField(db_column='Nombre', max_length=30)
    apellido = models.CharField(db_column='Apellido', max_length=30)
    sexo = models.CharField(db_column='Sexo', max_length=1)
    edad = models.IntegerField(db_column='Edad')

    class Meta:
        managed = True
        db_table = 'persona'


class Telefono(Persona):
    cod_tlf = models.AutoField(db_column='Cod_Tlf', primary_key=True)
    cod_area1 = models.PositiveIntegerField(db_column='Cod_Area1')
    cod_area2 = models.PositiveIntegerField(db_column='Cod_Area2', blank=True, null=True)
    num1 = models.IntegerField(db_column='Num1')
    num2 = models.IntegerField(db_column='Num2', blank=True, null=True)
    ci_related = models.ForeignKey(Persona, related_name='ci_linked', db_column='CI', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'telefono'

