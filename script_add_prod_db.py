import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geekshop.settings")
import django

django.setup()
from mainapp.models import Product, ProductCategory
import json

def check_blank_str(input_str, defaulf_str):
   return defaulf_str if input_str == '' else input_str

with open('example_prod.json', 'r') as f:
    data = json.loads(f.read())


list_category = [str(i) for i in list(ProductCategory.objects.all())]
data['image'] = check_blank_str(data['image'], '../static/img/no_photo.png')
data['category'] = check_blank_str(data['category'], 'no category')
print(data)
if data['category'] in list_category:
    data['category'] = ProductCategory.objects.all()[list_category.index(data['category'])]
else:
    new_category = ProductCategory(name=data['category'])
    new_category.save()
    data['category'] = new_category
category = ProductCategory.objects.all()[1]
new_prod = Product(
    category=data['category'],
    name=data['name'],
    image=data['image'],
    short_desc=data['short_desc'],
    description=data['description'],
    price=data['price'],
    quantity=data['quantity'],
)
print(list_category)
print(new_prod)
new_prod.save()
