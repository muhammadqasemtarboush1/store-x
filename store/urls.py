from django.urls import path

from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item_update'),
    # path('store/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
