from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    return render(request, 'core/home.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guardar el mensaje en la base de datos
            contact_message = form.save()
            
            # Aquí podrías añadir envío de email
            # send_contact_email(contact_message)
            
            # Mensaje de éxito
            messages.success(request, '¡Mensaje enviado con éxito! Te contactaremos pronto.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})