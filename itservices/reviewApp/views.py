from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Review, Profile, User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.views.generic import TemplateView
# from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'reviewApp/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'reviewApp/about.html', {'title': 'About Us'})

def contact(request):
	if request.method == 'POST':
		message = "Name: %s \r Email: %s \r Subject: %s  \r Message: %s \r" % (
			request.POST['Name'], 
			request.POST['Email'], 
			request.POST['Subject'], 
			request.POST['Message']
		)
		send_mail(
			'Contact Form',
			message,
			settings.EMAIL_HOST_USER,
			['radit2639@zohomail.eu'],
			fail_silently=False
		)
		messages.success(request, f'Message Sent!')
	return render(request, 'reviewApp/contact.html', {'title': 'Home'})

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
	paginate_by = 4

class ProductDetailView(LoginRequiredMixin, TemplateView):
	
	template_name = 'reviewApp/product_detail.html'

	def get_context_data(self, **kwargs):
		prod = self.kwargs['pk']
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['Products'] = Product.objects.filter(id=prod)
		context['Reviews'] = Review.objects.filter(product=prod)
		context['Action'] = Review.objects.filter(author=self.request.user, product=prod)
		return context

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ['name', 'brand', 'cost', 'category', 'releasedate', 'description', 'productphoto']
def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class ReviewListView(ListView):
	model = Review 
	template_name = 'reviewApp/review.html'
	context_object_name = 'reviews'
	ordering = ['-postdate']
	paginate_by = 4
		

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