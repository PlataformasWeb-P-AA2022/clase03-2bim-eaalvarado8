
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('matriculas', views.index, name='index'),

 ]
