from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('',notas,name='notas'),
    path('edit/<int:id>',notas_editar,name="editar_nota"),
    path('edit/',notas_editar,name="editar_nota"),
    path('delete/<int:id>',notas_borrar,name="borrar_nota"),
    path('delete/',notas_borrar,name="borrar_nota"),
    path('auditorias/',auditorias,name="auditorias"),
]