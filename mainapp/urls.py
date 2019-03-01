from django.conf.urls import url
from .views import product

urlpatterns = [
    url(r'^$', product, name='index'),
    url(r'^(\d+)/$', product, name='category'),
]