from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db import IntegrityError
from django.conf import settings
import requests

from .forms import RegistroUsuarioForm
from .models import Accion, Transaccion
from .alpaca_api import obtener_info_accion, realizar_orden

#from Componentes.app.sources import market_client


def home(request):
    return HttpResponse("<h1>Bienvenido al sistema financiero</h1><p><a href='/registro/'>Registrarse</a></p>")


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            try:
                usuario = form.save()
                auth_login(request, usuario)
                return redirect('home')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya está registrado.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'signup.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            auth_login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def comprar_accion(request, accion_id):
    accion = get_object_or_404(Accion, id=accion_id)

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))

        resultado_api = realizar_orden(accion.ticker, cantidad, tipo='buy')

        Transaccion.objects.create(
            usuario=request.user,
            accion=accion,
            tipo_orden='compra',
            estado='completado',
            cantidad=cantidad,
            precio_compra=accion.precio_actual
        )

        return render(request, 'confirmacion.html', {'resultado': resultado_api})

    return render(request, 'comprar_accion.html', {'accion': accion})

def lista_acciones(request):
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url)
        productos = response.json() if response.status_code == 200 else []
    except Exception:
        productos = []

    # Construimos la lista con un campo `id`
    acciones = []
    for item in productos:
        acciones.append({
            'id': item['id'],  # ← aquí
            'nombre_accion': item['title'],
            'ticker': item['id'],         # lo usas solo para mostrar  
            'precio_actual': item['price']
        })

    return render(request, 'acciones.html', {'acciones': acciones})
@login_required
def transacciones_usuario(request):
    transacciones = Transaccion.objects.filter(usuario=request.user).order_by('-fecha_transaccion')
    return render(request, 'transacciones_usuario.html', {'transacciones': transacciones})
