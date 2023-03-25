from django.shortcuts import render
from .models import Menu

def main(request):
    context = {
        'request': request,
    }
    return render(request, 'index.html', context)

def navigate(request, *args, **kwargs):
    discription = Menu.objects.get(slug=kwargs.get('slug')).description
    context = {
        'discription':discription,
    }
    return render(request, 'navigate.html', context)


# Create your views here.
