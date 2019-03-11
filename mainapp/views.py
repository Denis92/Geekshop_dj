from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket

# from basketapp.views import basket_viw


links_menu = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'product:index', 'name': 'Каталог'},
    {'href': 'contact', 'name': 'Контакты'},
]


# Create your views here.


def get_hot_offer():
    hot_offer = Product.objects.filter(hot_offer=True)
    return hot_offer.all()


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def main(request):
    basket = get_basket(request.user)

    context = {
        'link': links_menu,
        'basket': basket,
    }

    return render(request, 'mainapp/index.html', context=context)


def product(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu_prod = ProductCategory.objects.all()
    products = Product.objects.all()
    basket = get_basket(request.user)

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
            'hot_offer': get_hot_offer(),
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
        'hot_offer': get_hot_offer(),
    }
    return render(request, 'mainapp/product.html', context=context)


def product_page(request, pk=None):
    title = 'продукты'

    context = {
        'title': title,
        'link': links_menu,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product_page.html', context=context)


def contact(request):
    basket = get_basket(request.user)
    context = {
        'list_info': [1, 2, 3],
        'link': links_menu,
        'basket': basket,
    }
    return render(request, 'mainapp/contact.html', context=context)
