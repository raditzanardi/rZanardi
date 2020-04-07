from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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


