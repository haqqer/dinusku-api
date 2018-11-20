import pytest
import api_dinusku
import requests

def TestUsingRequestsHari():
    for i in range(1, 6):
        url = requests.post('http://academic.dinus.ac.id/home/perkuliahan_perharidansesi', data={'id_hari':i, 'id_sesi':2})
        assert url.status_code == 200
