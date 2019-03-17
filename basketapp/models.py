from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datatime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return f'{self.user} | {self.product} | количество : {self.quantity}'
    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def basket_total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return total_quantity

    @property
    def basket_total_cost(self):
        items = Basket.objects.filter(user=self.user)
        total_coast = sum(list(map(lambda x: x.product_cost, items)))
        return total_coast

class OrderUser(models.Model):
    # user_order = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datatime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    # def __str__(self):
        # return f'{self.user} | {self.product} | количество : {self.quantity}'


