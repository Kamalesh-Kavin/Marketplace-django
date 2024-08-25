from django.shortcuts import render
from item.models import Category, Item
from django.db.models import Count

# Create your views here.
def index(request):
    featured_products = Item.objects.filter(is_sold=False).order_by('-id')[:4]  # Example: Get the 5 most recent unsold items
    top_categories = Category.objects.annotate(num_items=Count('items')).order_by('-num_items')[:4]
    return render(request, 'index.html', {
        'featured_products': featured_products,
        'top_categories': top_categories,
    })

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')