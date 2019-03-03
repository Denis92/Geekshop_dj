import os
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

import json


def json_read(path_json, json_file):
    with open(os.path.join(path_json, json_file), 'r') as f:
        return json.loads(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        path_json = 'mainapp/json'
        json_file_categories = 'categories.json'
        json_file_products = 'product.json'
        categories = json_read(path_json, json_file_categories)

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = json_read(path_json, json_file_products)
        Product.objects.all().delete()
        for product in products:
            name_category = product['category']
            category_obj = ProductCategory.objects.get(name=name_category)
            product['category'] = category_obj
            new_product = Product(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('Denis', 'Denis@admin.com', 'toor', age=26)
        super_user.save()
