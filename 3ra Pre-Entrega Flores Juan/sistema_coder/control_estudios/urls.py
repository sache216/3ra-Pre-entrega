from django.urls import path
from control_estudios.views import listar_estudiantes

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
]