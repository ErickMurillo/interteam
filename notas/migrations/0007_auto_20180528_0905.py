# Generated by Django 2.0.5 on 2018-05-28 15:05

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_notas_vistas'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Foto'), (2, 'Video')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notas',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notas',
            name='vistas',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]