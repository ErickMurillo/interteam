# Generated by Django 3.2 on 2023-07-15 15:54

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import sorl.thumbnail.fields
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.IntegerField(choices=[(1, 'Foto'), (2, 'Video')])),
                ('foto', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='notas/')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Video (url)')),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha de publicación')),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('vistas', models.IntegerField(default=0, editable=False)),
                ('publicada', models.BooleanField()),
                ('correo_enviado', models.BooleanField(editable=False)),
                ('tags', taggit_autosuggest.managers.TaggableManager(blank=True, help_text='Separar elementos con "," ', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('temas', models.ManyToManyField(to='notas.Temas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'ordering': ['-fecha', '-id'],
            },
        ),
        migrations.CreateModel(
            name='ComentarioNotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('comentario', ckeditor_uploader.fields.RichTextUploadingField()),
                ('nota', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notas.notas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
