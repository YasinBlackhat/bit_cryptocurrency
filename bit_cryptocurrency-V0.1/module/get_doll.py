import requests
from bs4 import BeautifulSoup 

def _start_():
    try:
        res = requests.post('https://arzdigital.com/coins/')
        res_d = requests.post('https://arzdigital.com/coins/bitcoin/')
    except:
        return "check".lower()
    
    
    if res.status_code == 200 and res_d.status_code == 200:

        soup_d = BeautifulSoup(res_d.text, 'html.parser')
        soup = BeautifulSoup(res.text, 'html.parser')

        doll = soup.find('td',attrs={'class':'arz-coin-table-price-td arz-sort-value'})
        bit_D = soup_d.find('span',attrs={'class':'arz-sana-price'})

        ret_d = [str(doll.text), str(bit_D.text)]
        return ret_d

    elif res.status_code != 200:
        return int(res.status_code)
    elif res_d.status_code != 200:
        return int(res_d.status_code)
