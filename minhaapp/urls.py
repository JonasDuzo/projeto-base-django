from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_itens, name='lista_itens'),
    path('add/', views.add_item, name='add_item'),
]