from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLES, required=True, label="Tipo de usuario", widget=forms.Select(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
    }))
    username = forms.CharField(label="Nombre de usuario",widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
    }))
    email = forms.EmailField(label="Correo Electronico",widget=forms.EmailInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
    }))
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
    }))
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={
        'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 bg-white dark:bg-gray-700 dark:border-gray-600 dark:text-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
    }))

    class Meta:
        model = CustomUser
        fields = ['role', 'username', 'email', 'password1', 'password2']