from django.forms import ModelForm
from django import forms
from .models import Grain

class CoffeeForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['variety'].widget.attrs.update({'class': 'form_field'})
		self.fields['place'].widget.attrs.update({'class': 'form_field'})
		self.fields['region'].widget.attrs.update({'class': 'form_field'})
		self.fields['rediness'].widget.attrs.update({'class': 'form_field'})
		self.fields['img'].widget.attrs.update({'class': 'form_field'})


	class Meta:
		model = Grain
		fields = '__all__'
		