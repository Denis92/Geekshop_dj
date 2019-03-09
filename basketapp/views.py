from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    context = {}
    return render(request, 'basketapp.backet.html', context=context)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product)

    if basket:
        basket[0].quantity += 1
        print(basket[0])
        basket[0].save()
    else:
        new_basket = Basket(user=request.user, product=product)
        new_basket.quantity += 1
        new_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    context = {}
    return render(request, 'basketapp/basket.html', context=context)


def basket_viw(request):
    if request.user.is_authenticated:
        basket_res_all_price = 0
        basket_res_all_quantity = 0
        for i in range(1, len(Product.objects.all()) + 1):
            product = get_object_or_404(Product, pk=i)
            basket = Basket.objects.filter(user=request.user, product=product)
            basket_res_all_price += basket[0].quantity * product.price
            basket_res_all_quantity += basket[0].quantity
        return [basket_res_all_price, basket_res_all_quantity]
    else:
        return [None, None]
