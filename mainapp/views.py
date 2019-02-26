from django.shortcuts import render

list_product_img = [
    'img/product-11.jpg',
    'img/product-21.jpg',
    'img/product-31.jpg',
    'img/product-41.jpg',
    'img/product-5.jpg',
    'img/product-6.jpg',
    'img/product-11.jpg',
    'img/product-21.jpg',
    'img/product-31.jpg',
    'img/product-41.jpg',
    'img/product-5.jpg',

]
links_menu = [
    {'href': 'main', 'name': 'HOME'},
    #{'href': '#', 'name': 'HISTORY'},
    #{'href': '##', 'name': 'SHOWROOM'},
    {'href': 'product', 'name': 'PRODUCTS'},
    {'href': 'contact', 'name': 'CONTACT'},
   # {'href': '', 'name': "{% static 'img/search.png' %}"},
]

# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html', context={'link': links_menu})


def product(request):
    return render(request, 'mainapp/product.html', context={'list_img': list_product_img, 'link': links_menu})


def contact(request):
    return render(request, 'mainapp/contact.html', context={'list_info': [1, 2, 3], 'link': links_menu})
