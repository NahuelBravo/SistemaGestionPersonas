from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Proveedor, Producto
from django.shortcuts import render
from .verificaciones import *


# Create your views here.

def listado_productos(request):
    lista_productos = list(Producto.objects.select_related('proveedor').all())
    if request.method == 'POST':
        borrar_producto(request)
        lista_productos = list(Producto.objects.select_related('proveedor').all())
        return render(request, 'compras/listado_productos.html', {'productos': lista_productos})

    return render(request, 'compras/listado_productos.html', {'productos': lista_productos})


def agregar_producto(request):
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        verificar_producto(request)
    return render(request, 'compras/agregar_producto.html', {'proveedores': proveedores})


def listado_proveedores(request):
    lista_proveedores = list(Proveedor.objects.all())
    if request.method == 'POST':
        if borrar_proveedor(request):
            return redirect('/compras/proveedores/listado')
    return render(request, 'compras/listado_proveedores.html', {'proveedores': lista_proveedores})


def agregar_proveedor(request):
    errores = []
    proveedor = {'nombre_proveedor': "", 'cuit_proveedor': 0, 'celular_proveedor': 0}
    if request.method == 'POST':
        errores, proveedor = verificar_proveedor(request)
        if not errores:
            mensaje = "Proveedor agregado exitosamente"
            return render(request, 'compras/agregar_proveedor.html', {'mensaje': mensaje})
    return render(request, 'compras/agregar_proveedor.html',
                  {'errores': errores, 'proveedor': proveedor})
