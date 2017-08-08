# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from .models import TipoCurso
from .models import Curso


# Register your models here.
class cursosField(admin.ModelAdmin):
    list_display = ('idTipoCurso', 'cursoCode', 'cursoVideo', 'idCinta',
                    'descripcion',)
    list_filter = ['idTipoCurso__tipoCursoCode', 'idCinta__cintaCode']
    search_fields = ['idTipoCurso__tipoCursoCode', 'cursoCode', 'idCinta__cintaCode' ]


admin.site.register(TipoCurso)
admin.site.register(Curso,cursosField)