from .views import AnimalList, animal_detail, AnimalCreate, PenList, pen_detail, PenCreate, ZooList, zoo_detail, ZooCreate
from django.conf.urls import url


urlpatterns = [
	url(r'^animal_list/$',
		AnimalList.as_view(),
		name='petorganizer_animal_list'),

url(r'animal/create/$',
		AnimalCreate.as_view(),
		name='petorganizer_animal_create'),
	
	url(r'^animal/(?P<slug>[\w\-]+)/$',
		animal_detail,
		name='petorganizer_animal_detail'),

	url(r'^pen_list/$',
		PenList.as_view(),
		name='petorganizer_pen_list'),
	
	url(r'pen/create/$',
		PenCreate.as_view(),
		name='petorganizer_pen_create'),
	
	url(r'^pen/(?P<slug>[\w\-]+)/$',
		pen_detail,
		name='petorganizer_pen_detail'),


	url(r'^$',
		ZooList.as_view(),
		name='petorganizer_zoo_list'),

	url(r'zoo/create/$',
		ZooCreate.as_view(),
		name='petorganizer_zoo_create'),
	
	url(r'^zoo/(?P<slug>[\w\-]+)/$',
		zoo_detail,
		name='petorganizer_zoo_detail'),

]