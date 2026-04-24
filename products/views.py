from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def lista_productos(request):

    # Obtener datos base
    categorias = Category.objects.all()
    productos = Product.objects.all()

    categoria_id = request.GET.get("categoria")
    categoria = None

    # Filtrar por categoría si existe
    if categoria_id:
        categoria = get_object_or_404(Category, id=categoria_id)
        productos = productos.filter(category_id=categoria_id)

    # Contexto para el template
    context = {
        "categorias": categorias,
        "productos": productos,
        "categoria": categoria,
    }

    return render(request, "products/productos.html", context)
