# Generated by Django 2.0.5 on 2020-10-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20201026_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='enviar_correo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='publicada',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
