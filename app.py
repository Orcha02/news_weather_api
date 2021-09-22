#!/usr/bin/python3
from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit():
    city = '{}'.format(request.form['city'])
    if (city is None or city == ''):
        return render_template('index.html', news='', weather='')
    news = getNews(city)
    weather = getWeather(city)
    # Proceso
    return render_template('index.html', news=news, weather=weather)


def getNews(city):
    url = 'https://newsapi.org/v2/everything'
    payload = {'q': city, 'apiKey': '03befe7eb37f49ec98c8181311d51c01'}
    r = requests.get(url, params=payload)
    Author = ("AUTHOR: {}").format(r.json().get('articles')[0].get('author'))
    Title = ("TITLE: {}").format(r.json().get('articles')[0].get('title'))
    Description = ("DESCRIPTION: {}").format(r.json().get('articles')[0].get('description'))
    return Author + '\n' + Title + '\n' + Description

def getWeather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    payload = {'q': city, 'appid': '4b576d3c23ad7fba0b5fa4694e6edc1c'}
    r = requests.get(url, params=payload)
    L = ("LOCATION: {}, {}").format(r.json().get('name'), (r.json().get('sys').get('country')))
    W = ("WEATHER: {}").format(r.json().get('weather')[0].get('main'))
    D = ("DESCRIPTION: {}").format(r.json().get('weather')[0].get('description'))
    Tmp = ("TEMP: {}, FEELS LIKE: {}").format(r.json().get('main').get('temp'), (r.json().get('main').get('feels_like')))
    Mm = ("MAX TEMP: {}, MIN TEMP: {}").format(r.json().get('main').get('temp_max'), (r.json().get('main').get('temp_min')))
    P = ("PRESSURE: {}").format(r.json().get('main').get('pressure'))
    H = ("HUMIDITY: {}").format(r.json().get('main').get('humidity'))
    return L + '\n' + W + '\n' + D + '\n' + Tmp + '\n' + Mm + '\n' + P + '\n' + H


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
