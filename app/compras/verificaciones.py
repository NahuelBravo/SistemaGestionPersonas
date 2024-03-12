from .models import Proveedor, Producto
from django.http import HttpResponseNotFound


def verificar_producto(request):
    nombre = request.POST['txtNombre']
    precio = request.POST['nmbPrecio']
    stock = request.POST['nmbStock']
    proveedor_id = request.POST.get('txtProveedor')

    try:
        proveedor = Proveedor.objects.get(id=proveedor_id)
        producto, created = Producto.objects.get_or_create(
            nombre=nombre, precio=precio, proveedor=proveedor,
            defaults={'stock_actual': stock})
        if not created:
            producto.stock_actual += int(stock)
        producto.save()

    except Proveedor.DoesNotExist:
        return "el proveedor no existe"


def borrar_producto(request):
    producto_id = request.POST.get('producto_id')
    producto = Producto.objects.get(id=producto_id)

    try:
        producto.delete()
    except:
        return HttpResponseNotFound("Producto no encontrado")


def verificar_proveedor(request):
    nombre_proveedor = request.POST['txtRazon']
    cuit_proveedor = request.POST['nmbCuit']
    celular_proveedor = request.POST['nmbCel']

    if Proveedor.objects.filter(razon_social=nombre_proveedor).exists():
        return "Razón Social Inválida: La razón social ya pertenece a otro proveedor"
    elif Proveedor.objects.filter(cuit=cuit_proveedor).exists():
        return "CUIT Inválido: El CUIT ya pertenece a otro proveedor"
    elif Proveedor.objects.filter(celular=celular_proveedor).exists():
        return "Celular Inválido: El celular ya pertenece a otro proveedor"

    Proveedor.objects.create(razon_social=nombre_proveedor, cuit=cuit_proveedor, celular=celular_proveedor)


def borrar_proveedor(request):
    proveedor_id = request.POST.get('proveedor_id')
    proveedor = Proveedor.objects.get(id=proveedor_id)

    try:
        proveedor.delete()
    except:
        return HttpResponseNotFound("Proveedor no encontrado")
