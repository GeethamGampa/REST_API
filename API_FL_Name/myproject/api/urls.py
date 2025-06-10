from django.urls import path
from .views import FullNameAPIView

urlpatterns = [
    path('fullname/', FullNameAPIView.as_view(), name='fullname'),
]
