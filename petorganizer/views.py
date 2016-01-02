from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .models import Animal, Pen, Zoo
from .forms import AnimalForm, PenForm, ZooForm

class AnimalList(View):
	def get(self, request):
		return render(
			request,
			'petorganizer/animal_list.html',
			{'animal_list': Animal.objects.all()}
			)


def animal_detail(request, slug):
	animal = get_object_or_404(
		Animal, slug__iexact=slug)
	return render(
		request,
		'petorganizer/animal_detail.html',
		{'animal': animal}
		)


class AnimalCreate(View):
	form_class = AnimalForm
	template_name = 'petorganizer/animal_form.html'

	def get(self, request):
		return render(
			request,
			self.template_name,
			{'form': self.form_class()})
	def post(self, request):
		bound_form = self.form_class(request.POST)
		if bound_form.is_valid():
			new_animal = bound_form.save()
			return redirect(new_animal)
		else:
			return render(
				request,
				self.template_name,
				{'form': bound_form})

class PenList(View):
	def get(self, request):
		return render(
			request,
			'petorganizer/pen_list.html',
			{'pen_list': Pen.objects.all()}
			)


def pen_detail(request, slug):
	pen = get_object_or_404(
		Pen, slug__iexact=slug)
	return render(
		request,
		'petorganizer/pen_detail.html',
		{'pen': pen}
		)


class PenCreate(View):
	form_class = PenForm
	template_name = 'petorganizer/pen_form.html'

	def get(self, request):
		return render(
			request,
			self.template_name,
			{'form': self.form_class()})
	def post(self, request):
		bound_form = self.form_class(request.POST)
		if bound_form.is_valid():
			new_pen = bound_form.save()
			return redirect(new_pen)
		else:
			return render(
				request,
				self.template_name,
				{'form': bound_form})

class ZooList(View):
	def get(self, request):
		return render(
			request,
			'petorganizer/zoo_list.html',
			{'zoo_list': Zoo.objects.all()}
			)


def zoo_detail(request, slug):
	zoo = get_object_or_404(
		Zoo, slug__iexact=slug)
	return render(
		request,
		'petorganizer/zoo_detail.html',
		{'zoo': zoo}
		)

class ZooCreate(View):
	form_class = ZooForm
	template_name = 'petorganizer/zoo_form.html'

	def get(self, request):
		return render(
			request,
			self.template_name,
			{'form': self.form_class()})
	def post(self, request):
		bound_form = self.form_class(request.POST)
		if bound_form.is_valid():
			new_zoo = bound_form.save()
			return redirect(new_zoo)
		else:
			return render(
				request,
				self.template_name,
				{'form': bound_form})