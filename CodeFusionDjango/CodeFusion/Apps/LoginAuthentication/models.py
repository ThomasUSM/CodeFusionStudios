from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    # Agrega otros campos adicionales si es necesario

    def __str__(self):
        return self.username
    
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'profesor'})

    def __str__(self):
        return self.nombre
    