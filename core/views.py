from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
    featured_products = Item.objects.filter(is_sold=False).order_by('-id')[:5]  # Example: Get the 5 most recent unsold items
    return render(request, 'index.html', {'featured_products': featured_products})

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')