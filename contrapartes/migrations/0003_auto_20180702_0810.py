# Generated by Django 2.0.5 on 2018-07-02 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contrapartes', '0002_auto_20180618_1006'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contraparte',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='contraparte',
            name='font_color',
        ),
    ]
