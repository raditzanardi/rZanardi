from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView, ProductCreateView, ReviewListView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView, successView
urlpatterns =[
    path('', views.home, name='reviewApp-home'),
    path('about/', views.about, name='reviewApp-about'),
    path('contact/', views.contact, name='reviewApp-contact'),
    path('product', ProductListView.as_view(), name='reviewApp-product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('review/', ReviewListView.as_view(), name='reviewApp-review'),
    path('review/new/<int:pk>', ReviewCreateView.as_view(), name='review-create'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/update', ReviewUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete', ReviewDeleteView.as_view(), name='review-delete'),
    path('success/', successView, name='success'),
]