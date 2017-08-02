# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-01 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170801_1826'),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='idCinta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.Cinta', verbose_name='Grado deseable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='idTipoCurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.TipoCurso', verbose_name='Tipo curso'),
        ),
        migrations.AlterField(
            model_name='tipocurso',
            name='tipoCursoCode',
            field=models.CharField(max_length=200, unique=True, verbose_name='Tipo curso'),
        ),
    ]