# Generated by Django 2.0.5 on 2018-06-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actividad', models.CharField(max_length=200)),
                ('hora_inicio', models.TimeField(verbose_name='Hora inicio')),
                ('hora_fin', models.TimeField(verbose_name='Hora fin')),
                ('descripcion', models.CharField(max_length=600)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='agendas.Agendas')),
            ],
        ),
    ]
