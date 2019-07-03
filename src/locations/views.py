from django.shortcuts import render
import requests 

def home(request):
    response = requests.get('http://gd.geobytes.com/AutoCompleteCity?callback=JSONP_CALLBACK&q=')
    geodata = response.json()
    return render(request, 'core/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })

