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

class ReviewListView(TemplateView):
	template_name = 'reviewApp/review.html'
	def get_context_data(self, **kwargs):
		context = super(ReviewListView, self).get_context_data(**kwargs)
		context['Reviews'] = Review.objects.all().order_by('-postdate')
		return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['rating', 'reviewtext']
	def form_valid(self, form, **kwargs):
		form.instance.product_id = self.kwargs['pk']
		form.instance.author = self.request.user
		form.instance.profile = self.request.user.profile
		return super().form_valid(form)

class ReviewDetailView(DetailView):
	model = Review

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Review
	fields = ['rating', 'reviewtext']
	def form_valid(self, form, **kwargs):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Review
	success_url = '/product'
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False