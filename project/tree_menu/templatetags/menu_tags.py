from django import template
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    menu_item = MenuItem.objects.filter(name=menu_name).last()

    menu_items = []
    if current_url.startswith(menu_item.get_absolute_url()):
        menu_items += _get_parent_items(menu_item)
    menu_items.append(menu_item)
    return mark_safe(_draw_menu(menu_items, current_url))


def _draw_menu(menu_items, current_url, number=0):
    menu_html = '<ul>\n'
    item = menu_items[number]
    is_active = current_url.startswith(item.get_absolute_url())
    if is_active:
        children_html = '<ul>'
        if item.children.exists():
            for children in item.children.all():
                children_html += f'<li><a href="{children.get_absolute_url()}">{children.name}</a></li>\n'
        children_html += '</ul>'
        menu_html += (f'<li class="active">\n'
                      f'<a href="{item.get_absolute_url()}">{item.name}</a>\n{children_html}</li>')
    else:
        if number < len(menu_items) - 1:
            menu_html += (f'<li>'
                          f'<a href="{item.get_absolute_url()}">{item.name}</a>'
                          f'{_draw_menu(menu_items, current_url, number+1)}'
                          f'</li>')
        else:
            menu_html += (f'<li>'
                          f'<a href="{item.get_absolute_url()}">{item.name}</a>'
                          f'</li>')
    menu_html += '</ul>'
    return menu_html


def _get_parent_items(menu_item):
    parent_items = []
    while menu_item.parent:
        menu_item = menu_item.parent
        parent_items.insert(0, menu_item)
    return parent_items
