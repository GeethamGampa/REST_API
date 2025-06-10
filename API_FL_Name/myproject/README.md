Full Name API using Django REST Framework
This is a simple Django REST API project I built to practice creating, running, and testing an API that combines first_name and last_name into a full name.

What this API does
Accepts a POST request with a list of people (each having first_name and last_name).

Returns a response with each person’s full name, neatly formatted.

Example input:
[
  {"first_name": "Geetham", "last_name": "Gampa"},
  {"first_name": "Mahanthi", "last_name": "Rajana"}
]


Example output:
{
  "full_names": ["Geetham Gampa", "Mahanthi Rajana"]
}

What I did — Step by Step

1. Created a virtual environment
python -m venv Myenv
Myenv\Scripts\activate  

2. Installed Django and Django REST Framework
pip install django djangorestframework


 3. Created Django project and app
 django-admin startproject myproject
cd myproject
python manage.py startapp api

4. Added apps in settings.py
In myproject/settings.py, I added these to INSTALLED_APPS:
'rest_framework',
'api',

5. Wrote API logic in api/views.py
Here I wrote the logic to:

Loop through a list of names

Format each one as full name (with capitalization)

Return the result

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FullNameAPIView(APIView):
    def post(self, request):
        data = request.data

        if not isinstance(data, list):
            return Response({'error': 'Expected a list of names.'}, status=status.HTTP_400_BAD_REQUEST)

        full_names = []
        for person in data:
            first_name = person.get('first_name')
            last_name = person.get('last_name')

            if not first_name or not last_name:
                return Response({'error': 'Each item must include first_name and last_name.'}, status=status.HTTP_400_BAD_REQUEST)

            full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
            full_names.append(full_name)

        return Response({'full_names': full_names}, status=status.HTTP_200_OK)


6. Created app-level URL file api/urls.py

from django.urls import path
from .views import FullNameAPIView

urlpatterns = [
    path('fullname/', FullNameAPIView.as_view(), name='fullname'),
]


7. Linked API URLs in myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


 8. Ran migrations and started the server
 python manage.py migrate
python manage.py runserver


9. Tested the API in Postman
URL:
http://127.0.0.1:8000/api/fullname/


Method:
POST

Body (raw → JSON):
[
  {"first_name": "Geetham", "last_name": "Gampa"},
  {"first_name": "Mahanthi", "last_name": "Rajana"},
  {"first_name": "Esha", "last_name": "Annapureddy"},
  {"first_name": "Jaunty", "last_name": "Pilli"}
]

Response:
{
  "full_names": [
    "Geetham Gampa",
    "Mahanthi Rajana",
    "Esha Annapureddy",
    "Jaunty Pilli"
  ]
}

How I fixed a 500 error
At first, I got this error:

AttributeError: 'list' object has no attribute 'get'

I fixed it by using a for loop to handle each dictionary inside the list, instead of trying to call .get() on the list itself.

What I learned
How to create a Django REST API from scratch

How to handle POST requests and JSON input

How to validate data and return custom JSON responses

How to test APIs in Postman