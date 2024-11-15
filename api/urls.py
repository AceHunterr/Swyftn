from django.urls import path
from .views import (
    ImageHashCreateAPIView,
    ImageDataListCreateAPIView,
    ImageDataRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('hash/', ImageHashCreateAPIView.as_view(), name='image-hash'),
    path('images/', ImageDataListCreateAPIView.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDataRetrieveUpdateDestroyAPIView.as_view(), name='image-detail'),
]
