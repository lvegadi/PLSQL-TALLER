from django.urls import URLPattern, path
from .views import *

urlpatterns = [
    path('',notas,name='notas'),
]