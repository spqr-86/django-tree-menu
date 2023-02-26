from django.views.generic import DetailView, ListView
from .models import MenuItem


class MenuDetailView(DetailView):
    model = MenuItem
    context_object_name = 'menu'


class MenuListView(ListView):
    model = MenuItem
