
"""Market Data URL Configuration"""

from django.urls import path
from marketdata import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addstock', views.addstock, name="addstock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('deletestock', views.deletestock, name="deletestock"),
   
]

