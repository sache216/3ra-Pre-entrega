from django.shortcuts import render, redirect
from django.urls import reverse
from control_estudios.models import Estudiante, Curso
from control_estudios.forms import CursoFormulario
from django.db.models import Q


def listar_estudiantes(request):
    contexto = {
        "profesor": "Juan",
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response

def listar_cursos(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response

def crear_curso_V1(request):
   if request.method == "POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'])
        curso.save()
        url_exitosa = reverse('lista_cursos')
        return redirect(url_exitosa)
   else:  # GET
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_cursos_a_mano.html',
        context=contexto,
    )
    return http_response

def crear_curso(request):
   if request.method == "POST":
       formulario = CursoFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           comision = data["comision"]
           curso = Curso(nombre=nombre, comision=comision)  # lo crean solo en RAM
           curso.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_cursos')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = CursoFormulario()
   http_response = render(
       request=request,
       template_name='control_estudios/formulario_curso.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        # cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        cursos = Curso.objects.filter(
            Q(nombre__icontains=busqueda) | Q(comision__contains=busqueda)
        )

        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response
