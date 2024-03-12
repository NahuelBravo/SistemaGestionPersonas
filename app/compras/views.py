from django.shortcuts import render, redirect
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
        borrar_proveedor(request)
        lista_proveedores = list(Proveedor.objects.all())
        return render(request, 'compras/listado_proveedores.html', {'proveedores': lista_proveedores})

    return render(request, 'compras/listado_proveedores.html', {'proveedores': lista_proveedores})


def agregar_proveedor(request):
    if request.method == 'POST':
        verificar_proveedor(request)

    return render(request, 'compras/agregar_proveedor.html')
