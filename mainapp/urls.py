from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.product, name='index'),
    path('category/<int:pk>/', mainapp.product, name='category'),
    path('category/<int:pk>/page/<int:page>/', mainapp.product, name='page'),
    path('product_page/<int:pk>/', mainapp.product_page, name='product_page'),
    path('contact/', mainapp.contacts, name='contact')
]