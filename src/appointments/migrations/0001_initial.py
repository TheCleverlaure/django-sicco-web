# Generated by Django 2.2.2 on 2019-12-26 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('date', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitasAsistidas',
            fields=[
                ('cod_cita_asistidas', models.AutoField(db_column='Cod_CitaA', primary_key=True, serialize=False)),
                ('hora', models.TimeField(db_column='Hora')),
                ('precio', models.FloatField(db_column='Precio')),
                ('asistencia', models.CharField(db_column='Asistencia', max_length=10)),
                ('cod_paciente', models.IntegerField(db_column='Cod_Paciente')),
                ('cod_fecha', models.IntegerField(db_column='Cod_Fecha')),
                ('cod_cita', models.IntegerField(db_column='Cod_Cita')),
            ],
            options={
                'db_table': 'citas_asistidas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CitasAusentes',
            fields=[
                ('cod_cita_ausentes', models.AutoField(db_column='Cod_CitaAu', primary_key=True, serialize=False)),
                ('hora', models.TimeField(db_column='Hora')),
                ('precio', models.FloatField(db_column='Precio')),
                ('asistencia', models.CharField(db_column='Asistencia', max_length=10)),
                ('cod_paciente', models.IntegerField(db_column='Cod_Paciente')),
                ('cod_fecha', models.IntegerField(db_column='Cod_Fecha')),
                ('cod_cita', models.IntegerField(db_column='Cod_Cita')),
            ],
            options={
                'db_table': 'citas_ausentes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CitasCanceladas',
            fields=[
                ('cod_cita_canceladas', models.AutoField(db_column='Cod_CitaC', primary_key=True, serialize=False)),
                ('hora', models.TimeField(db_column='Hora')),
                ('precio', models.FloatField(db_column='Precio')),
                ('asistencia', models.CharField(db_column='Asistencia', max_length=10)),
                ('cod_paciente', models.IntegerField(db_column='Cod_Paciente')),
                ('cod_fecha', models.IntegerField(db_column='Cod_Fecha')),
                ('cod_cita', models.IntegerField(db_column='Cod_Cita')),
            ],
            options={
                'db_table': 'citas_canceladas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('cod_cita', models.AutoField(db_column='Cod_Cita', primary_key=True, serialize=False)),
                ('hora', models.TimeField(db_column='Hora')),
                ('precio', models.FloatField(db_column='Precio')),
                ('asistencia', models.CharField(blank=True, db_column='Asistencia', max_length=10, null=True)),
                ('cod_fecha', models.ForeignKey(blank=True, db_column='Cod_Fecha', null=True, on_delete=django.db.models.deletion.CASCADE, to='date.Fecha', unique=True)),
                ('cod_paciente', models.ForeignKey(blank=True, db_column='Cod_Paciente', null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.Paciente', unique=True)),
            ],
            options={
                'db_table': 'citas',
                'managed': True,
            },
        ),
    ]