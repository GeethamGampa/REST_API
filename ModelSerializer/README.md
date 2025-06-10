## Django REST API – Product List using ModelSerializer

This project is a simple REST API built using Django and Django REST Framework. It uses a model serializer to return a list of products with their details and also supports creating new products through a single endpoint.

## Features

- View all products (GET /api/products/)

- Add new products (POST /api/products/)

- Uses Django model + DRF ModelSerializer

- Built with class-based views (ListCreateAPIView)


## Step-by-Step Setup & What I Did

1. Created the Django project and app
```
django-admin startproject myproject
cd myproject
python manage.py startapp api
```

2. Installed required packages
Make sure Django and Django REST Framework are installed:
```
pip install django djangorestframework
```

 3. Updated settings.py

In myproject/settings.py, added 'rest_framework' and 'api' to INSTALLED_APPS:
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

4. Created the Product model

api/models.py:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
```
5. Created the model serializer
 
api/serializers.py:
```
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

- ModelSerializer automatically maps all model fields.

6. Created the class-based view

api/views.py:
```
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

- ListCreateAPIView allows both GET (list) and POST (create) operations.

7. Created API URLs

api/urls.py:
```
from django.urls import path
from .views import ProductList

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
]
```

8. Included app URLs in the project

myproject/urls.py:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

9. Ran migrations and started the server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## API Testing with Postman
```
GET Products
URL: http://127.0.0.1:8000/api/products/
```

Method: GET

## Response:
```
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 1000,
    "description": "A high-end laptop"
  },
  ...
]
```

## What I Learned

- How to create Django models

- How to use ModelSerializer to auto-generate serializers

- How to use generic views like ListCreateAPIView

- How to test APIs with Postman
