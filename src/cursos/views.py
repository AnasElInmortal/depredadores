# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
#from profiles import models

from models import Curso
from models import TipoCurso

from django.shortcuts import render

# Create your views here.
class MostrarCurso(LoginRequiredMixin, generic.TemplateView):
    template_name = "cursos/show_course.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        idCinta = user.profile.idCinta

        if idCinta is not None:
            video = self.kwargs.get('id')
            if video:
                elVideo = Curso.objects.filter(idCinta__lte = idCinta ).filter(pk=video)
                if elVideo:
                    kwargs["video"] = get_object_or_404(Curso, pk=video)
                else:
                    kwargs["error"] = 'No se encontró ningún video. Intente con otro.'


            cursos = Curso.objects.filter(idCinta__lte = idCinta ).order_by('idTipoCurso','idCinta')
            lista = []
            for curso in cursos:
                if curso.idTipoCurso_id not in lista:
                    lista.append(curso.idTipoCurso_id)

            kwargs["tiposCurso"] = TipoCurso.objects.filter(pk__in=lista).order_by('pk')
            #Question.objects.filter( pub_date__lte=timezone.now() ).order_by('-pub_date')[:5]
            kwargs["show_user"] = user
            kwargs["cursos"] = cursos
        else:
            kwargs["error"] = 'No tiene cinta asignada. Solicitelo al administrador del sitio.'

        return super(MostrarCurso, self).get(request, *args, **kwargs)
