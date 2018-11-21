import pytest
import requests

def test_url():
    url = requests.get('https://dinus-api.herokuapp.com')
    assert url.json() == {'status':'ok'}

if __name__ == '__main__':
    pytest.main()
