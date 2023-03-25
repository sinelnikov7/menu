from django import template
from django.db.models import Prefetch
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from menu.models import Menu

register = template.Library()

@register.simple_tag
def draw_menu(types):
    """Функция для получения меню"""
    template = f'{types}.html'
    menu = Menu.objects.get(name=types)
    context = {
        'menu': menu.children.all(),
    }
    return render_to_string(template, context)

@register.simple_tag
def while_tag(type):
    """Функция для заполнения шаблона"""
    obj = type
    response = f'<div hidden id=this_{obj.slug}>'
    def fn(obj):
        nonlocal response
        for i in obj.children.all():
            if  i.has_children == False:
                response += f'<div id={i.slug} class="endppoint"><a href="{i.slug}">{i.name}</a>'
            if i.has_children:
                response += f'<div id={i.slug} class="within" onclick="fn(event)">{i.name}<div hidden id=this_{i.slug}>'
                fn(i)
                response += f'</div>'
            response += f'</div>'
    fn(obj)
    response += f'</div>'
    return mark_safe(response)