# Generated by Django 2.2.2 on 2019-12-26 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitaTienePago',
            fields=[
                ('cod_cita', models.ForeignKey(db_column='Cod_Cita', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='appointments.Citas')),
            ],
            options={
                'db_table': 'cita_tiene_pago',
                'managed': False,
            },
        ),
    ]
