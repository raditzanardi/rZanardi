from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	fullname = models.CharField(max_length=100, null=True)
	dob = models.DateField(null=True)
	address = models.TextField(null=True)
	city = models.CharField(max_length=100, null=True)
	country = models.CharField(max_length=100, null=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'Profile for {self.user.username}'

