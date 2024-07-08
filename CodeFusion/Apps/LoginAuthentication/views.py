from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from axes.models import AccessAttempt
from django.utils import timezone

def index_view(request):
    return render(request, 'LoginAuthentication/index.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Por favor, inicia sesión.')
            return redirect('iniciar_sesion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'LoginAuthentication/crear_cuenta.html', {'form': form})

def recuperacion_view(request):
    return render(request, 'LoginAuthentication/recuperacion_cuenta.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            mensaje_error="Usuario o Contraseña Incorrectos."
            return render(request, 'LoginAuthentication/iniciar_sesion.html',{"mensaje_error":mensaje_error})
    else:
        return render(request, 'LoginAuthentication/iniciar_sesion.html')

@login_required
def home_view(request):
    return render(request, 'LoginAuthentication/home.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')

def increment_failed_attempts(username, ip_address, user_agent, failures):
    AccessAttempt(username=username, ip_address=ip_address, user_agent=user_agent, attempt_time=timezone.now(), failures_since_start=failures).save()

def reset_failed_attempts(username):
    AccessAttempt.objects.filter(username=username).delete()