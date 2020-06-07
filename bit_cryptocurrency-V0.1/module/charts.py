import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from colorama import Fore, init
import os
from bs4 import BeautifulSoup
import seaborn as sns
sns.set()

def _start_init():
    try:
        res = requests.get('https://arzdigital.com/coins/')
        sub = BeautifulSoup(res.text, 'html.parser')
    except:
        return "check".lower()

    mk1 = 'app_BTC'
    f3 = os.path.exists('app_BTC')
    if f3 == False :
        mk = os.mkdir(mk1)
    if res.status_code == 200:
        print('\n'+Fore.MAGENTA+' Bitcoin weekly chart this week \n')
        ur = sub.find('img',attrs={'alt':'bitcoin-chart'})
        url = ur['data-src']
        filename = "app_BTC/IMG.png"
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        img = 'app_BTC/IMG.png'
        plt.imshow(mpimg.imread(img))
        plt.show()
        os.remove("app_BTC/IMG.png")
    elif res.status_code != 200:
        return int(res.status_code)
