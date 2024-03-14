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
    errores = []
    proveedor = {'nombre_proveedor': "", 'cuit_proveedor': 0, 'celular_proveedor': 0}

    if Proveedor.objects.filter(razon_social=nombre_proveedor).exists():
        errores.append("Razón Social Inválida: La razón social ya pertenece a otro proveedor")
        proveedor['nombre_proveedor'] = ""
        proveedor['cuit_proveedor'] = cuit_proveedor
        proveedor['celular_proveedor'] = celular_proveedor

    if Proveedor.objects.filter(cuit=cuit_proveedor).exists():
        errores.append("CUIT Inválido: El CUIT ya pertenece a otro proveedor")
        proveedor['nombre_proveedor'] = nombre_proveedor
        proveedor['cuit_proveedor'] = 0
        proveedor['celular_proveedor'] = celular_proveedor

    if Proveedor.objects.filter(celular=celular_proveedor).exists():
        errores.append("Celular Inválido: El celular ya pertenece a otro proveedor")
        proveedor['nombre_proveedor'] = nombre_proveedor
        proveedor['cuit_proveedor'] = cuit_proveedor
        proveedor['celular_proveedor'] = 0

    if not errores:
        proveedor, creado = Proveedor.objects.get_or_create(
            razon_social=nombre_proveedor,
            cuit=cuit_proveedor,
            celular=celular_proveedor
        )
        if creado:
            return errores, proveedor
        else:
            errores.append("El proveedor ya existe")
            return errores, proveedor
    else:
        return errores, proveedor


def borrar_proveedor(request):
    proveedor_id = request.POST.get('proveedor_id')
    proveedor = Proveedor.objects.get(id=proveedor_id)

    try:
        proveedor.delete()
        return True
    except Proveedor.DoesNotExist:
        return False
