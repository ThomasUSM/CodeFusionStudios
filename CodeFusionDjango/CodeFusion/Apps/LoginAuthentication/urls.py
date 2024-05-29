from django.urls import path
from .views import login_view, home_view, logout_view, index_view, register_view, recuperacion_view

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='iniciar_sesion'),
    path('registrarse/', register_view, name='crear_cuenta'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('recuperacion_cuenta/', recuperacion_view, name='recuperacion_cuenta'),
]