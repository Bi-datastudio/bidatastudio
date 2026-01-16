from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo electrónico")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    company = models.CharField(max_length=100, blank=True, null=True, verbose_name="Empresa")
    message = models.TextField(verbose_name="Mensaje")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de envío")
    is_read = models.BooleanField(default=False, verbose_name="Leído")
    
    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.email}"