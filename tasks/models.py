from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo personalizado de Usuario
class Usuario(AbstractUser):
    ROLE_CHOICES = [
        ('cliente', 'Cliente'),
        ('comisionista', 'Comisionista'),
        ('auditor', 'Auditor'),
        ('admin', 'Administrador'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# Modelo de Acción bursátil
class Accion(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    empresa = models.CharField(max_length=100)
    nombre_accion = models.CharField(max_length=100)
    sector = models.CharField(max_length=50, blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_accion} ({self.ticker}) - ${self.precio_actual}"


# Modelo de Transacción
class Transaccion(models.Model):
    TIPO_ORDEN_CHOICES = [
        ('compra', 'Compra'),
        ('venta', 'Venta'),
    ]
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('programada', 'Programada'),
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='transacciones'
    )
    comisionista = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comisiones'
    )
    accion = models.ForeignKey(Accion, on_delete=models.CASCADE)
    tipo_orden = models.CharField(max_length=10, choices=TIPO_ORDEN_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    cantidad = models.PositiveIntegerField()
    precio_compra = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    precio_venta = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    fecha_transaccion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.usuario.username} - "
            f"{self.get_tipo_orden_display()} {self.cantidad} "
            f"de {self.accion.ticker} ({self.estado})"
        )
