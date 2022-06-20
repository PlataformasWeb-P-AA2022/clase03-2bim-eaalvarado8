from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import Matricula

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # matriculas 
    matriculas = Matricula.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'matriculas': matriculas, 'numero_matriculas': len(matriculas)}
    return render(request, 'index.html', informacion_template)