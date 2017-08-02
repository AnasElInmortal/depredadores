from django.conf.urls import url
from . import views

app_name = 'cursos'

urlpatterns = [
    url(r'^$', views.MostrarCurso.as_view(), name='mostrarCursos'),
    url(r'^(?P<id>[0-9]+)$', views.MostrarCurso.as_view(), name='reproducir'),
]