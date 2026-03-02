from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import render, get_object_or_404

def lista_productos(request):
    categorias = Category.objects.all()
    productos = Product.objects.all()

    categoria_id = request.GET.get("categoria")
    categoria = None

    if categoria_id:
        categoria = get_object_or_404(Category, id=categoria_id)
        productos = productos.filter(category_id=categoria_id)
        

    context = {
        "categorias": categorias,
        "productos": productos,
        "categoria": categoria,
    }

    return render(request, "products/productos.html", context)