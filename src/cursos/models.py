# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from profiles.models import Cinta

User = get_user_model()
# Create your models here.

class TipoCurso(models.Model):
    tipoCursoCode = models.CharField(max_length=200, unique=True, null=False, verbose_name="Tipo curso")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tipoCursoCode


class Curso(models.Model):
    idTipoCurso = models.ForeignKey(TipoCurso, on_delete=models.CASCADE, verbose_name="Tipo curso")
    cursoCode = models.CharField(max_length=200, unique=True)
    cursoVideo = models.FileField ('Subir video',
                                upload_to='video_cursos/%Y-%m-%d/',
                                null=False,
                                blank=True)
    descripcion = models.TextField(blank=True, null=True)
    idCinta = models.ForeignKey(Cinta, on_delete=models.CASCADE, verbose_name="Grado deseable")

    def __str__(self):
        return self.cursoCode

