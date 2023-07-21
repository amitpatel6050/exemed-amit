from django import forms
from .models import Contact_us
from .models import Employee_reg
# from .models import Nrgp_entry


# creating a form
class Contact_usForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		model = Contact_us
		# model = Nrgp_entry

		# specify fields to be used
		fields = '__all__'

class Employee_regForm(forms.ModelForm):




	# create meta class
	class Meta:
	
		# specify model to be used
		model = Employee_reg
		# model = Nrgp_entry

		# specify fields to be used
		fields = '__all__'