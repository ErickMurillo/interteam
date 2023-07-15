# Generated by Django 3.2 on 2023-07-15 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biblioteca', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='tematica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notas.temas'),
        ),
        migrations.AddField(
            model_name='archivos',
            name='usuario',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
