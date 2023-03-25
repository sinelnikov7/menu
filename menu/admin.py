from django.contrib import admin
from .models import  Menu


class MenuAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'parent', 'has_children')
    fields = ['name', 'slug', 'description', 'parent']

admin.site.register(Menu, MenuAdmin)

# Register your models here.
