from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLES = (
        ('student', 'Alumno'),
        ('teacher', 'Profesor'),
    )
    role = models.CharField(max_length=7, choices=ROLES, default='student')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Agrega related_name aquí
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Agrega related_name aquí
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser',
    )
