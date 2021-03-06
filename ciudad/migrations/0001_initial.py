# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-30 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('icono', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('background', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('habitantes', models.IntegerField()),
                ('region', models.CharField(choices=[(b'I', b'Tarapaca'), (b'II', b'Antofagasta'), (b'III', b'Atacama'), (b'IV', b'Coquimbo'), (b'V', b'Valparaiso'), (b'VI', b'O Higgins'), (b'VII', b'Maule'), (b'VIII', b'Bio-Bio'), (b'IX', b'La Araucania'), (b'X', b'Los Lagos'), (b'XI', b'Aysen'), (b'XII', b'Magallanes'), (b'RM', b'Metropolitana'), (b'XIV', b'Los Rios'), (b'XV', b'Arica y parinacota')], max_length=10)),
                ('clima', models.CharField(max_length=100)),
                ('url', models.CharField(default=b'', max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('descripcion', models.CharField(default=b'', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_variable', models.CharField(choices=[(b'char', b'caracter'), (b'int', b'numero entero'), (b'float', b'numero con pocos decimales')], max_length=6)),
                ('var_int', models.IntegerField(blank=True, null=True)),
                ('var_char', models.CharField(blank=True, max_length=10, null=True)),
                ('var_float', models.FloatField(blank=True, null=True)),
                ('creado', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modificado', models.DateTimeField(editable=False, null=True)),
                ('fecha_indicador', models.DateTimeField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudad.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('estado', models.CharField(max_length=10)),
                ('icono', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudad.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='dato',
            name='indicador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudad.Indicador'),
        ),
    ]
