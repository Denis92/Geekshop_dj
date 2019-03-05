from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from basketapp.views import basket_viw

list_product_img = [
    {'href': 'img/Raspberry-Pi-3_small.jpg', 'name': 'Raspberry Pi 3 Model B'},
    {'href': 'img/Raspberry-Pi-3_plus_small.jpg', 'name': 'Raspberry Pi 3 Model B+'},
    {'href': 'img/Pi-Zero-W-Tilt_small.jpg', 'name': 'Raspberry Pi Zero'},
]
links_menu = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'product:index', 'name': 'Каталог'},
    {'href': 'contact', 'name': 'Контакты'},
]

# Create your views here.

def main(request):
    context = {
        'link': links_menu,
        'price_all': basket_viw(request)[0],
        'quantity_all': basket_viw(request)[1],
    }
    return render(request, 'mainapp/index.html', context= context)


def product(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu_prod = ProductCategory.objects.all()
    products = Product.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'title': title,
            'links_menu_prod': links_menu_prod,
            'category': category,
            'products': products,
            'link': links_menu,
            'basket': basket,
            'price_all': basket_viw(request)[0],
            'quantity_all': basket_viw(request)[1],
        }
        return render(request, 'mainapp/products_list.html', context=context)

    same_products = Product.objects.all()[1:3]

    context = {
        'title': title,
        'links_menu_prod': links_menu_prod,
        'same_products': same_products,
        'link': links_menu,
        'products': products,
        'basket': basket,
        'price_all': basket_viw(request)[0],
        'quantity_all': basket_viw(request)[1],
    }
    return render(request, 'mainapp/product.html', context=context)


def contact(request):
    context = {
        'list_info': [1, 2, 3],
        'link': links_menu,
        'price_all': basket_viw(request)[0],
        'qauntity_all': basket_viw(request)[1],
    }
    return render(request, 'mainapp/contact.html', context= context)

