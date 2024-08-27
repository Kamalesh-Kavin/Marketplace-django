from django.shortcuts import render, get_object_or_404
from .models import Item, Category

def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    related_items = Item.objects.filter(category=item.category).exclude(id=item.id)[:4]
    return render(request, 'detail.html', {'item': item, 'related_items': related_items})