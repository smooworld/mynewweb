from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class EditProfileForm(UserChangeForm):
	"""
	This class is used to hold data objects information of
	member changing details.
	"""
	password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))
	birth_date= forms.DateField(label='', widget=forms.SelectDateWidget)
	bio = forms.CharField(label="", widget=forms.TextInput())
	image = forms.ImageField()
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password', )

			
class ProfileForm(UserChangeForm):
	class Meta:
		model = Profile
		fields = ('bio','image', 'birth_date')



class SignUpForm(UserCreationForm):
	"""This class is used to hold data objects information of new user"""
	email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
	first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(label="",max_length=100 ,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'UserName'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only</small></span>'


		
		self.fields['password1'].label = ''
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
		self.fields['password1'].help_text = '<span class = "form-text text-muted"><small><ul><li>Your password can\'t be too similar to your other personal information</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password</li><li>Your password can\'t be entirely numeric</li></ul></small></span>'


		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].label = ''
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].help_text = '<span class = "form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

