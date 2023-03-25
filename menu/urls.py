from django.urls import path, include
from .views import main, navigate

app_name = 'menu'

urlpatterns = [
    path('', main, name='main'),
    path('<str:slug>', navigate, name='navigate')
]