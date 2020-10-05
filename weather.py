from flask import Flask
from flask import render_template
import time
import json
import urllib
import os
import requests

app = Flask(__name__)

def get_weather():
    url_weath = "http://api.openweathermap.org/data/2.5/forecast?q=London&appid=72248f167f6d06f5f1da1a7e3a029e5b"
    http = urllib.request.urlopen(url_weath).read()
    #response = requests.get(url)
    return http
@app.route("/")
def index():
    data= json.loads(get_weather())
    day = time.strftime('%d %B', time.localtime(data.get('list')[0].get('dt')))
    mini = data.get('list')[0].get('main').get('temp_min')
    maxi = data.get('list')[0].get('main').get('temp_max')
    description = data.get('list')[0].get('weather')[0].get('description')
    
    return render_template('index.html', day=day, mini=mini, maxi=maxi, description=description)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port=port, debug=True)