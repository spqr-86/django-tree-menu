from django.views.generic import DetailView
from .models import MenuItem


class MenuDetailView(DetailView):
    model = MenuItem
    context_object_name = 'menu'
