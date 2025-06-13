# tasks/admin.py
from django.contrib import admin
from .models import Usuario, Accion, Transaccion

admin.site.register(Usuario)
admin.site.register(Accion)
admin.site.register(Transaccion)

