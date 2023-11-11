from django.urls import path
from control_estudios.views import (
    listar_estudiantes, listar_cursos, crear_curso, buscar_cursos)

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
]