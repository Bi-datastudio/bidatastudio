from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '¿En qué podemos ayudarte?',
                'rows': 5
            }),
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'message': 'Mensaje',
        }