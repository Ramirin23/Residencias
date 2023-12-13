# En tu archivo urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('view/', views.lista_narrativas, name="lista_narrativas")
]
