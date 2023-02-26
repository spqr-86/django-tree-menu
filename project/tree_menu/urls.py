from django.urls import path
from .views import MenuDetailView, MenuListView

urlpatterns = [
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu_item'),
    path('', MenuListView.as_view()),
]
