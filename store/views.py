from audioop import reverse
from dataclasses import fields

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from pyexpat import model

from .models import Item


# Create your views here.

class ItemListView(ListView):
    template_name = 'store/item_list.html'
    model = Item


class ItemDetailView(DetailView):
    template_name = 'store/item_detail.html'
    model = Item


class ItemCreateView(CreateView):
    template_name = 'store/item_create.html'
    model = Item
    fields = ['name', 'purchaser', 'description']


class ItemUpdateView(UpdateView):
    template_name = 'store/item_update.html'
    model = Item
    fields = ['name', 'purchaser', 'description']


class ItemDeleteView(DeleteView):
    template_name = 'store/item_delete.html'
    model = Item
    success_url = reverse_lazy('item_list')
