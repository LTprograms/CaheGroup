from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to="cursos/", blank=True, null=True)

    def admin_image(self):
        return mark_safe('<a href="{url}"><img src="{url}" width="{width}" height={height} /></a>'.format(
            url=self.imagen.url,
            width=100,
            height=100,
            ))
    admin_image.short_description = 'Image'
    admin_image.allow_tags = True

class VideoCurso(models.Model):
    titulo = models.CharField(max_length=50)
    video = models.FileField(upload_to="cursos/")
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)