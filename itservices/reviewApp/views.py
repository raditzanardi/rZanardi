from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Review, Profile, User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
# from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'reviewApp/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'reviewApp/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def products(request):
    all_products = {
		'products': Product.objects.all()
	}
	
    return render(request, 'reviewApp/products.html', all_products)

class ProductListView(ListView):
    model = Product
    template_name = 'reviewApp/product.html'
    context_object_name = 'products'
    ordering = ['-releasedate']

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ['name', 'brand', 'cost', 'category', 'releasedate', 'description', 'productphoto']
def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

