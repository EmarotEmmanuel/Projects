import requests # type: ignore
from django.http import JsonResponse
from django.conf import settings
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_location(request):
    GEOLOCATION_API_URL = f'https://ipinfo.io/json?token={settings.GEOLOCATION_API_TOKEN}'
    
    try:
      response = requests.get(GEOLOCATION_API_URL)
      data = response.json()
      loc = data.get('loc', '0,0').split(',')
      latitude, longitude = float(loc[0]), float(loc[1])
      
      return JsonResponse({
          'city' : data.get('city', 'N/A'),
          'region' : data.get('region', 'N/A'),
          'country' : data.get('country', 'N/A'),
          'latitude': latitude,
          'longitude': longitude,
      })
    except requests.RequestException:
      return JsonResponse({'Error' : 'Error fetching Location Data'}, status = 500)

def indexed_body (request):
    return render(request, "Tracker.html")
    