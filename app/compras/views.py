from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Proveedor, Producto
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


# Create your views here.

def listado_productos(request):
    lista_productos = list(Producto.objects.select_related('proveedor').all())

    return render(request, 'compras/listado_productos.html', {'productos': lista_productos})


def agregar_producto(request):
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        precio = request.POST['nmbPrecio']
        stock = request.POST['nmbStock']
        proveedor_id = request.POST.get('txtProveedor')
        proveedor = Proveedor.objects.get(id=proveedor_id)

        Producto.objects.create(nombre=nombre, precio=precio, stock_actual=stock, proveedor=proveedor)

    return render(request, 'compras/agregar_producto.html', {'proveedores': proveedores})


def listado_proveedores(request):
    lista_proveedores = list(Proveedor.objects.all())

    return render(request, 'compras/listado_proveedores.html', {'proveedores': lista_proveedores})


def agregar_proveedor(request):
    if request.POST:
        nombre_proveedor = request.POST['txtRazon']
        cuit_proveedor = request.POST['nmbCuit']
        celular_proveedor = request.POST['nmbCel']

        Proveedor.objects.create(razon_social=nombre_proveedor, cuit=cuit_proveedor, celular=celular_proveedor)

    return render(request, 'compras/agregar_proveedor.html')
