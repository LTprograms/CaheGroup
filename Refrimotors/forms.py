from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    asunto = forms.CharField(max_length=50)
    mensaje = forms.CharField(max_length=500)

    