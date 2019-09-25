from flask_restful import Resource
from . import *

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

class Jadwal_proses:
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

class Jadwal(Resource):
    def get(self, hari, sesi):
        data =  Jadwal_proses(hari,sesi)
        kuliah = data.jadwal()
        data_jadwal = jadwal_to_json(kuliah)
        return data_jadwal