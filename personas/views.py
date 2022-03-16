import django
from django.shortcuts import render
from django.db import connection
# Create your views here.
def notas(request):
    data = {
        'notas':listar_notas()
    }
    return render(request,'notas/crud.html',data)

def listar_notas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor() # Cursor que llama
    out_cur = django_cursor.connection.cursor() # cursor que recibe
    cursor.callproc('SP_LISTAR_NOTAS',[out_cur])

    lista  = []
    for fila in out_cur:
        lista.append(fila)
    return lista