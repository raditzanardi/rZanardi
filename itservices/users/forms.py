from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Row, Column, Submit

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	address = forms.CharField()
	dob = forms.DateField(
		widget=forms.TextInput(
			attrs={'type': 'date'}
		), label='Date of Birth'
	)
	def __init__(self, *args, **kwargs):
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(
				Div(Field('fullname'), css_class='col-md-6',),
				Div(Field('dob'), css_class='col-md-6',),
				css_class='row',
			),
			Div(
				Div(Field('address'), css_class='col-md-6',),
				Div(Field('city'), css_class='col-md-6',),
				css_class='row',
			),
			Div(
				Div(Field('country'), css_class='col-md-6',),
				Div(Field('image'), css_class='col-md-6',),
				css_class='row',
			),
		)
		super(ProfileUpdateForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Profile
		fields = ['fullname', 'dob', 'address', 'city', 'country', 'image']
		labels = {
			'fullname': 'Full Name',
			'address': 'Address',
			'city': 'City',
			'country': 'Country',
			'image': 'Profile Photo',
		}