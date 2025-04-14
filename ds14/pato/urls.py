from django.contrib import admin
from django.urls import path
from .views import PatoListCreateAPIView, PatoDetailAPIView  # Importa a view correta

urlpatterns = [
    path('pato/', PatoListCreateAPIView.as_view(), name='pato-list-create'),
    path('patos/<int:pk>/', PatoDetailAPIView.as_view(), name='pato-especifico'),  # Usa a view certa
]
