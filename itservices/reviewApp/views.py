from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'reviewApp/home.html')

def about(request):
    return render(request, 'reviewApp/about.html')

def contact(request):
    return render(request, 'reviewApp/contact.html')

def products(request):
    return render(request, 'reviewApp/products.html')