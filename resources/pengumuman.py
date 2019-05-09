from . import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getallinfo():
    driver = webdriver.Chrome()
    driver.get("https://dinus.ac.id/getallinfo")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = soup.find('table')
    driver.close()
    count=0
    data = {}
    for i in content.find_all('tr'):
        count=count+1
        data = {
            'id': count,
            'title': i.text.split()[1:-2],
            'date': i.text.split()[-1]
        }
    return data


class Pengumuman(Resource):
    def get(self):
        data_pengumuman = getallinfo()
        return data_pengumuman 
    