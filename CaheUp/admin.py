from django.contrib import admin
from .models import *

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "admin_image", "nombre", "descripcion")
class VideoCursoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "descripcion")

admin.site.register(Curso, CursoAdmin)
admin.site.register(VideoCurso, VideoCursoAdmin)