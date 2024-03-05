from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.http import HttpResponse
from django.urls import path
from django.utils.html import format_html
from .models import *
from django import forms

class AlquilerForm(forms.ModelForm):    
    class Meta:
        fields = ['cliente', "maquinaria", "destino", "fin", "cantidad", "descuento"]
        model = Alquiler
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cliente._meta.fields]

class MaquinariaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Maquinaria._meta.fields]

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "maquinaria", "cantidad", 'inicio', 'fin', "pdf")
    form = AlquilerForm

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.generar_pdf(form.cleaned_data)
        with open("./COTIZACION DE VICAMAR.pdf", "rb") as file:
            obj.pdf_url.save("COTIZACION DE VICAMAR.pdf", File(file), save=False)
        os.remove("./COTIZACION DE VICAMAR.pdf")
        return super().save_model(request, obj, form, change)

admin.site.register(Cliente, ClienteAdmin) 
admin.site.register(Maquinaria, MaquinariaAdmin)  
admin.site.register(Alquiler, AlquilerAdmin) 