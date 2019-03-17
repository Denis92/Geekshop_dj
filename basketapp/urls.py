from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    path('viw/', basketapp.basket_viw, name='viw'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
    path('order_user/add', basketapp.get_order_user, name='order_user'),
    path('remove_order', basketapp.remove_order, name='remove_order'),
]