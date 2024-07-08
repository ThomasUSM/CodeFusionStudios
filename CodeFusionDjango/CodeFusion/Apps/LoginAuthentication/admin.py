from django.contrib import admin
from .models import CustomUser, Clase
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Clase)

