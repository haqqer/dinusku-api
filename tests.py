import pytest
import requests

def test_url():
    url = requests.post('http://academic.dinus.ac.id/home/perkuliahan_perharidansesi', data={'id_hari':1, 'id_sesi':2})
    assert url.status_code == 200

if __name__ == '__main__':
    pytest.main()
