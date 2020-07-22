import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore
# import library

def _init_():
    listof_curr = []
    in1 = float(input(Fore.LIGHTYELLOW_EX+'Input value : ')) # Get value : example( 200 )
    model1 = str(input('Origin Currency Type : ')).upper() 
    print('To')
    model2 = str(input('Destination Currency Type : ')).upper()
    print(Fore.LIGHTYELLOW_EX+'Please Wating ...')
    res = requests.post('https://arzdigital.com/coins/calculator/?convert=%i-%s-to-%s' % (in1, model1, model2)) 
    sub = BeautifulSoup(res.text, 'html.parser')
    mreq = sub.find('input',attrs={'type' : "text",'pattern' : '^\d{1,3}(,\d{3})*$'})
    mreq = mreq['value']
    change1 = sub.find('input',attrs={'type' : "text",'pattern' : '^(\.|\d{1,3}(,\d{3})*)*$'}) 
    change1 = change1['value']
    change2 = sub.find('input', attrs={'pattern' : "^\d{1,3}(,\d{3})*$"})
    change2 = change2['value']
    change3 = sub.find('h4', attrs={'class' : "xtomans"})
    change3 = str(change3.text).replace('به ارزش : ', '').replace(' تومان', '').strip()
    change4 = sub.find('span', attrs={'class' : "price"})
    change4 = change4.text
    change5 = 'Worth '+change3+' tomans'
    listof_curr = [str(in1), model1, model2, change4, change5, str(mreq)]
    return listof_curr
# a = _init_()
