"""
URL configuration for UsuariosFinanciero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tasks.views import lista_acciones, registro_usuario, comprar_accion, home,iniciar_sesion
from django.contrib.auth.decorators import login_required

# UsuariosFinanciero/urls.py o tasks/urls.py
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('acciones/', views.lista_acciones, name='lista_acciones'),
    path('comprar/<int:accion_id>/', views.comprar_accion, name='comprar_accion'),
]

