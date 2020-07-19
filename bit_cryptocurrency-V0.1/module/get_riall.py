import requests
from bs4 import BeautifulSoup 
# import library

def _start_():
    try: 
        res = requests.post('https://arzdigital.com/coins/')
        res_d = requests.post('https://arzdigital.com/coins/bitcoin/')
        # post request for get data
    except:
        return "check".lower()
    
    
    if res.status_code == 200 and res_d.status_code == 200: # Check response statuse code (200, 404, 403, 503, ...)

        soup_d = BeautifulSoup(res_d.text, 'html.parser')
        soup = BeautifulSoup(res.text, 'html.parser')

        rial = soup.find('td',attrs={'class':'arz-coin-table-rial-price-td arz-sort-value'}) # find and get rial price
        bit_D = soup_d.find('span',attrs={'class':'arz-sana-price'}) # find and get bit coin. price

        ret_d = [str(rial.text).replace('تومان', ''), str(bit_D.text)]
        return ret_d

    elif res.status_code != 200:
        return int(res.status_code)
    elif res_d.status_code != 200:
        return int(res_d.status_code)
