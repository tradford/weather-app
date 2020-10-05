from flask import Flask
from flask import render_template
import time
import json
import urllib
import os
import requests

app = Flask(__name__)
def get_coords():
    url_id = "http://api.openweathermap.org/data/2.5/forecast?id=524901&cnt=10&appid=72248f167f6d06f5f1da1a7e3a029e5b"
    info = urllib.request.urlopen(url_id).read()
    return info
def get_weather(lat):
    #url_weath = "72248f167f6d06f5f1da1a7e3a029e5b"
    url_weath = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon=-104.984703&exclude=minutely,hourly,current&appid=72248f167f6d06f5f1da1a7e3a029e5b".format(lat)
    http = urllib.request.urlopen(url_weath).read()
    #response = requests.get(url)
    
    return http
@app.route("/")
@app.route("/<findlat>")
def index(findlat="39.739151"):
    data= json.loads(get_weather(findlat))
    coordinates = data['lat']['lon']
    forecast_list = []
    for d in data.get('daily'):
        dayd = time.strftime('%d %B', time.localtime(d.get('dt')))
        mini = d.get('temp').get('min')
        maxi = d.get('temp').get('max')
        description = d.get('weather')[0].get('description')
        forecast_list.append((dayd,mini,maxi,description))
    
    return render_template('index.html', len=len(forecast_list), forecast_list=forecast_list, coordinates=coordinates)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port=port, debug=True)