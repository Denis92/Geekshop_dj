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
        basket[0].quantity +=1
        basket[0].save()
    else:
        new_basket = Basket(user=request.user, product=product)
        new_basket.quantity += 1
        new_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    context = {}
    return render(request, 'basketapp/basket,html', context=context)
