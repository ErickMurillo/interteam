# Generated by Django 2.0.5 on 2018-05-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrapartes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajero',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]