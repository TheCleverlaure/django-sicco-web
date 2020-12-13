from django.db import models
from persona.models import Persona

class Usuario(Persona):
    idusuario = models.CharField(db_column='IDUsuario', primary_key=True, max_length=50)
    password = models.CharField(db_column='Contrase�a', max_length=50)
    tipo_usuario = models.CharField(db_column='Tipo_Usuario', max_length=22)
    pregunta1 = models.CharField(db_column='Pregunta1', max_length=45)
    pregunta2 = models.CharField(db_column='Pregunta2', max_length=45)
    respuesta1 = models.CharField(db_column='Respuesta1', max_length=45)
    respuesta2 = models.CharField(db_column='Respuesta2', max_length=45)
    ci_related = models.OneToOneField(Persona, models.CASCADE, db_column='CI')

    class Meta:
        managed = True
        db_table = 'usuario'
