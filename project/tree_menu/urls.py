from django.urls import path
from .views import MenuDetailView

urlpatterns = [
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu_item'),
]
