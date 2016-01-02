from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Zoo (models.Model):
	name = models.CharField(
		max_length=31,
		unique=True,)
	owner = models.CharField(
		max_length=31,
		default='some owner',)
	slug = models.SlugField(
		max_length=31,
		unique=True,
		help_text='A label for URL config')
	def __str__(self):
			return self.name.title()
	def get_absolute_url(self):
		return reverse('petorganizer_zoo_detail',
						kwargs={'slug': self.slug})
	class Meta:
		ordering = ['name']


class Pen (models.Model):
	name = models.CharField(
		max_length=31,
		unique=True)
	slug = models.SlugField(
		max_length=31,
		unique=True,
		help_text='A label for URL config')
	acreage = models.IntegerField()
	zoo = models.ForeignKey(Zoo, editable=True, default=1)
	climate = models.CharField(
		max_length=31)
	def __str__(self):
			return self.name.title()
	def get_absolute_url(self):
		return reverse('petorganizer_pen_detail',
						kwargs={'slug': self.slug})
	class Meta:
		ordering = ['name']

class Animal (models.Model):
	name = models.CharField(
		max_length=31, 
		unique=True)
	species = models.CharField(
		max_length=31,
		default='cowform')
	slug = models.SlugField(
		max_length=31,
		unique=True,
		help_text='A label for URL config')
	sound = models.CharField(
		max_length=31)
	weapon = models.CharField(
		max_length=31)
	attack = models.IntegerField()
	speed = models.IntegerField()
	img = models.URLField()
	nat_climate = models.CharField(
		max_length=31)
	food = models.CharField(
		max_length=31)
	makes = models.CharField(
		max_length=31)
	pen = models.ForeignKey(Pen, editable=True, default=1)
	def __str__(self):
			return self.name.title()
	def get_absolute_url(self):
		return reverse('petorganizer_animal_detail',
						kwargs={'slug': self.slug})
	class Meta:
		ordering = ['name']