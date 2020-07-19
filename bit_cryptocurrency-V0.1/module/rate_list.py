from bs4 import BeautifulSoup
from colorama import Fore
import requests
import os
# import library

def _getdes_():
    os.system('clear')
    print(Fore.LIGHTYELLOW_EX+'''
    ██╗     ██╗███████╗████████╗     ██████╗ ███████╗    ██████╗  █████╗ ████████╗███████╗███████╗
    ██║     ██║██╔════╝╚══██╔══╝    ██╔═══██╗██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝
    ██║     ██║███████╗   ██║       ██║   ██║█████╗      ██████╔╝███████║   ██║   █████╗  ███████╗
    ██║     ██║╚════██║   ██║       ██║   ██║██╔══╝      ██╔══██╗██╔══██║   ██║   ██╔══╝  ╚════██║
    ███████╗██║███████║   ██║       ╚██████╔╝██║         ██║  ██║██║  ██║   ██║   ███████╗███████║
    ╚══════╝╚═╝╚══════╝   ╚═╝        ╚═════╝ ╚═╝         ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝ \n'''

                            ,Fore.LIGHTBLUE_EX+'''\n                            Display currency encryption display''')
def _pritnt_():
    input(Fore.LIGHTGREEN_EX+'Press Enter to get the information...')
    print('\n')
    res = requests.post('https://arzdigital.com/coins/')
    sub = BeautifulSoup(res.text, 'html.parser')
    change1 = sub.find_all('tr', attrs={'class' : 'arz-coin-tr arz-sort-value-row arz-fiat-parent'})
    row1 = '**********************************************************************************************************'
    print(Fore.LIGHTYELLOW_EX+'|',Fore.LIGHTCYAN_EX+'           NAME             ',Fore.LIGHTYELLOW_EX+'||',Fore.LIGHTMAGENTA_EX+'            Price $            ',Fore.LIGHTYELLOW_EX+'||',Fore.LIGHTBLUE_EX+'            Price Toman            ',Fore.LIGHTYELLOW_EX+'|')
    print('|******************************||*********************************||*************************************|')
    for i in change1:
        a = str(i.text).split('\n')
        a = list(filter(None, a))
        ro1 = (len(row1) - len(a[1])) - 79 # Obtain spatial distance1
        ro2 = (len(row1) - len(a[2])) - 76 # Obtain spatial distance2
        ro3 = (len(row1) - len(a[3])) - 73 # Obtain spatial distance3
        n = Fore.LIGHTYELLOW_EX+'|',Fore.LIGHTCYAN_EX+str(a[1]),ro1*' ',Fore.LIGHTYELLOW_EX+'||'
        tom = str(a[3]).replace('تومان', ' Toman')

        print(Fore.LIGHTYELLOW_EX+'|',Fore.LIGHTCYAN_EX+a[1],ro1*' ',Fore.LIGHTYELLOW_EX+ # Creat and show column
        '||',Fore.LIGHTMAGENTA_EX+a[2],ro2*' ',Fore.LIGHTYELLOW_EX+'||',Fore.LIGHTBLUE_EX+tom,ro3*' ',Fore.LIGHTYELLOW_EX+'|')
        print('|------------------------------||---------------------------------||-------------------------------------|')

# END
