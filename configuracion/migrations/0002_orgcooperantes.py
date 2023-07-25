# Generated by Django 3.2.20 on 2023-07-24 20:52

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgCooperantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', sorl.thumbnail.fields.ImageField(upload_to='org-coop/')),
            ],
            options={
                'verbose_name': 'Organización Cooperante',
                'verbose_name_plural': 'Organizaciones Cooperantes',
            },
        ),
    ]