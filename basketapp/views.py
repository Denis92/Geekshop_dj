from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket, OrderUser
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from mainapp.views import links_menu


@login_required
def basket(request):
    basket = Basket.objects.filter(user=request.user).order_by('product__category')

    context = {
        'basket': basket,
        'link': links_menu,
    }
    return render(request, 'basketapp/basket.html', context=context)


@login_required
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
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('product:product_page', args=[pk]))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

        context = {
            'basket': basket_items,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', context=context)

        return JsonResponse({'result': result})


@login_required
def get_order_user(request):
    # product = get_object_or_404(Product)
    basket = Basket.objects.filter(user=request.user)
    print(basket)
    for item in basket:
        print(item.product)
        order_record = OrderUser.objects.filter(product=item.product)
        print(order_record)
        # if order_record:
        #     order_record[0].quantity = item.quantity
        #     order_record[0].save()
        # else:
        new_order = OrderUser(product=item.product)
        new_order.quantity = item.quantity
        new_order.save()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(reverse('basket:remove_order'))

@login_required
def remove_order(request):
    basket = Basket.objects.filter(user=request.user)
    print(basket)
    for item in basket:
        print(item.product)
        order_record = OrderUser.objects.filter(product=item.product)
        order_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
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


