from django.urls import path
from . import views

urlpatterns = [
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('crear-cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('recuperacion-cuenta/', views.recuperacion_cuenta, name='recuperacion_cuenta'),
    path('', views.index, name='index'),
]
