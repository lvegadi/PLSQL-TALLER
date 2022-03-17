import django
import cx_Oracle
from django.shortcuts import render
from django.db import connection
# Create your views here.


def notas(request):

    data = {
        'notas': listar_notas(),
        'alumnos': listar_alumnos(),
        'asignaturas': listar_asignaturas()
    }

    if request.method == 'POST':
        alumno = request.POST.get('alumno')
        asignatura = request.POST.get('asignatura')
        year = request.POST.get('year')
        n1 = request.POST.get('n1')
        n2 = request.POST.get('n2')
        n3 = request.POST.get('n3')
        salida = agregar_nota(alumno, asignatura, year, n1, n2, n3)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['alumnos'] = listar_alumnos()
        else:
            data['mensaje'] = 'No se pudo guardar'
    #editar_nota(43,41, 1, 2025, 5, 5, 5)
    # eliminar_nota(43)
    return render(request, 'notas/crud.html', data)


def notas_editar(request, id=None):
    if id is not None:
        data = {
            'alumnos': listar_alumnos(),
            'id': id,
            'asignaturas': listar_asignaturas()

        }
        if request.method == 'POST':
            alumno = request.POST.get('alumno')
            asignatura = request.POST.get('asignatura')
            year = request.POST.get('year')
            n1 = request.POST.get('n1')
            n2 = request.POST.get('n2')
            n3 = request.POST.get('n3')
            salida = editar_nota(id, year, n1, n2, n3)
            if salida == 1:
                data['mensaje'] = 'editado correctamente'

            else:
                data['mensaje'] = 'No se pudo guardar'
        return render(request, 'notas/editar.html', data)
    else:
        return notas(request)


def notas_borrar(request, id=None):
    if id is not None:
        salida = eliminar_nota(id)
    return notas(request)


def auditorias(request):
    data = {
        'auditorias': listar_auditorias(),
    }
    return render(request, 'notas/auditorias.html', data)


# Metodos para llamar a los cursores
def listar_notas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()  # Cursor que llama
    out_cur = django_cursor.connection.cursor()  # cursor que recibe
    cursor.callproc('SP_LISTAR_NOTAS', [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_alumnos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()  # Cursor que llama
    out_cur = django_cursor.connection.cursor()  # cursor que recibe
    cursor.callproc('SP_LISTAR_ALUMNOS', [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_asignaturas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()  # Cursor que llama
    out_cur = django_cursor.connection.cursor()  # cursor que recibe
    cursor.callproc('SP_LISTAR_ASIGNATURAS', [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_auditorias():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()  # Cursor que llama
    out_cur = django_cursor.connection.cursor()  # cursor que recibe
    cursor.callproc('SP_LISTAR_AUDITORIAS', [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_nota(alumno, asignatura, year, n1, n2, n3):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_NOTAS', [
                    alumno, asignatura, year, n1, n2, n3, salida])
    return salida.getvalue()


def editar_nota(nota, year, n1, n2, n3):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_EDITAR_NOTAS', [
                    nota, year, n1, n2, n3, salida])
    return salida.getvalue()


def eliminar_nota(nota):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_NOTAS', [nota, salida])
    return salida.getvalue()
