#   -*- coding: utf-8 -*-
import requests

def Weather(city):

    if type(city) != type("city"):
        return

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8d833f001f321580188ec4a56538e0ba&units=metric&lang=it'.format(city)

    data = requests.get(url).json()

    info = {
        'Nazione': data['sys']['country'],
        'Tempo': data['weather'][0]['description'],
        'Temperatura': data['main']['temp'],
        'Pressione': data['main']['pressure'],
        'Umidita': data['main']['humidity']
    }

    return info
