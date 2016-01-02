from .models import Zoo, Pen, Animal
from django import forms

class SlugCleanMixin:
	def clean_slug(self):
		new_slug = (
			self.cleaned_data['slug'].lower())
		if new_slug == 'create':
			raise ValidationError(
				'Slug may not be called "create".')
		return new_slug

class ZooForm(
			SlugCleanMixin, forms.ModelForm):
	class Meta:
		model = Zoo
		fields = '__all__'

class PenForm(
			SlugCleanMixin, forms.ModelForm):
	class Meta:
		model = Pen
		fields = '__all__'

class AnimalForm(
			SlugCleanMixin, forms.ModelForm):
	class Meta:
		model = Animal
		fields = '__all__'