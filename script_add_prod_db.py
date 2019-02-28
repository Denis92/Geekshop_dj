import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geekshop.settings")
import django

django.setup()
from mainapp.models import Product, ProductCategory
import json

with open('example_prod.json', 'r') as f:
    data = json.loads(f.read())

category = ProductCategory.objects.all()[1]
new_prod = Product(
    category=category,
    name=data['name'],
    short_desc=data['short_desc'],
    description=data['description'],
    price=data['price'],
    quantity=data['quantity']
)
new_prod.save()
