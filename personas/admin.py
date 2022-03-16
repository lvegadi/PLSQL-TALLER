from django.contrib import admin
from .models import Alumno, Nota, Auditoria, Asignatura

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Nota)
admin.site.register(Asignatura)
admin.site.register(Auditoria)
