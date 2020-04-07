from django.shortcuts import render
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