from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
	category = models.CharField(max_length=100)
	releasedate = models.DateField()
	description = models.TextField()
	productphoto = models.ImageField(default='products/default_product.jpg', upload_to='products')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk':self.pk})

class Review(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	rating = models.PositiveSmallIntegerField(default=1, validators = [MinValueValidator(1), MaxValueValidator(5)])
	reviewtext = models.TextField()
	postdate = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'Review for {self.product} by {self.author} on {self.postdate}'

	def get_absolute_url(self):
		return reverse('review-detail', kwargs={'pk':self.pk})
