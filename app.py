from flask import Flask, jsonify, request
# from quart import Quart
import requests 
from bs4 import BeautifulSoup
import json
from pprint import pprint
from flask_cors import CORS
import re

# app = Quart(__name__)
app = Flask(__name__)
CORS(app)

def jadwal_to_json(data):
    data_jadwal = []
    temp = []
    i=0
    for data in data:
        i=i+1
        temp = {
            "id": i,
            "makul" : (re.findall('>\s\W(.*?)<', str(data)))[0].strip(), 
            "ruang" : (re.findall('[0-9]<br/>(.+[0-9A-Z].\w+)', str(data))),
            "kelompok" : (re.findall('([A-Z][0-9]+.[0-9]+)', str(data)))[0],
            "link": data['href']
        }
        data_jadwal.append(temp)     
    return data_jadwal

class Jadwal:
    def __init__(self, hari, sesi):
        self.hari = hari
        self.sesi = sesi

    def jadwal(self):
        with open("data_jadwal_dan_sesi.json") as f:
             data = json.loads(f.read())
        
        id_hari = data['id_hari'][self.hari]
        id_sesi = data['id_sesi'][self.sesi]
        url = requests.post('http://academic.dinus.ac.id/home/perkuliahan_perharidansesi', data={'id_hari':id_hari, 'id_sesi':id_sesi})
        soup = BeautifulSoup(url.text, 'html.parser')
        title = soup.findAll('div', class_='col-md-3')
        kuliah = []
        for i in title:
            temp = i.find('a')
            kuliah.append(temp)
        return kuliah

@app.route('/')
def home():
    return "DATA UDINUS"

@app.route('/<hari>/<sesi>')
def jadwal_get(hari, sesi):
    data =  Jadwal(hari,sesi)
    kuliah = data.jadwal()
    data_jadwal = jadwal_to_json(kuliah)
    return jsonify(data_jadwal)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")