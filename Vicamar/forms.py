from django import forms

class CotizacionForm(forms.Form):
    cliente = forms.CharField(max_length=150)
    ruc = forms.CharField(max_length=15)
    destino = forms.CharField(max_length=50)
    contacto = forms.CharField(max_length=50)
    