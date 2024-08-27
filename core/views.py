from django.shortcuts import render, redirect
from item.models import Category, Item
from django.db.models import Count
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})