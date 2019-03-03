from django.shortcuts import render
from .models import ProductCategory, Product

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
    return render(request, 'mainapp/index.html', context={'link': links_menu})


def product(request, pk=None):
    print(pk)
    products = Product.objects.all()
    return render(request, 'mainapp/product.html', context={'products': products, 'list_img': list_product_img, 'link': links_menu})


def contact(request):
    return render(request, 'mainapp/contact.html', context={'list_info': [1, 2, 3], 'link': links_menu})

