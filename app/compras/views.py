from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor, Producto

# Create your views here.


def listado_productos(request,):
    lista_productos = list(Producto.objects.select_related('proveedor').all())
    return render(request, 'compras/listado_productos.html',{'productos': lista_productos})


def agregar_producto(request):
    return render(request, 'compras/agregar_producto.html')


def listado_proveedores(request):
    return render(request, 'compras/listado_proveedores.html')


def agregar_proveedor(request):
    return render(request, 'compras/agregar_proveedor.html')
