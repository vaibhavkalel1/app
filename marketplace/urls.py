from django.urls import path
from . import views

urlpatterns = [
    path('', views.pencil_list, name='pencil_list'),
    path('sell/', views.sell_pencil, name='sell_pencil'),
]
