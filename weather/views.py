import requests
from django.shortcuts import render
from  .models import City
from .forms import CityForm

def index(request):
	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()
	print(cities)

	weather_data = []

	for city in cities:
		url = 'http://api.openweathermap.org/data/2.5/weather?q='+city.name+'&units=metric&APPID=6169d48251197975732f77247af50079'
		r = requests.get(url).json()
		city_weather = {
			'city' : city.name,
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)
	context = {'weather_data' : weather_data, 'form' : form}
	return render(request, 'weather/weather.html', context)