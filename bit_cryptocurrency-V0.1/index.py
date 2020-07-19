# Follow me github.com/YasinBlackhat
import os
import sys
import time
# import library

try:
    from colorama import Fore # Check library 
except:
    print("Install colorama Lib.      *pip install colorama*")
    sys.exit()

try:
    import requests # Check library 
except:
    print(Fore.RED+"Install requests Lib.      *pip install requests*")
    sys.exit()

try:
    # Check and import modules
    from des import header,Exit,infobit,dollar,rial,Ex,chart,cur,hl,exchanger,info_change
    from module import get_doll,charts,get_riall,get_currenc,exchang,rate_list
except:
    print(Fore.RED+"Humm. ERROR[404]       Please try to Clone repositorie in Git hub AA*")
    print(Fore.LIGHTCYAN_EX+"       https://github.com/YasinBlackhat")
    sys.exit()

row = True # var loop
while row: # loop
    os.system('clear') # clear command line
    try:
        header.baner() # Show Baner
    except KeyboardInterrupt: # Error CTRL+C
        Exit._ret_()
    except:
        print(Fore.RED+"Humm. [ERROR]404       Please try to Clone repositorie in Git hub *")
        print(Fore.LIGHTCYAN_EX+"       https://github.com/YasinBlackhat")
        sys.exit()
    try:
        print(Fore.LIGHTMAGENTA_EX+"Please Choose a Plane... \n")
        time.sleep(0.1)
        print(Fore.LIGHTYELLOW_EX+'[1] Bit Coin Information             \n')
        time.sleep(0.1)
        print(Fore.LIGHTYELLOW_EX+'[2] Bit Coin Changer                \n')
        time.sleep(0.1)
        print(Fore.LIGHTYELLOW_EX+'[3] Bit Blackhat Help                \n')
        time.sleep(0.1)
        print(Fore.LIGHTYELLOW_EX+'[4] Exit                             \n')
        time.sleep(0.1)
        # Show Menu list1


    except KeyboardInterrupt:
        Exit._ret_()

    except:
        print(Fore.LIGHTRED_EX+'Problems running the program')
        sys.exit()
    try:
        _set_ = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m'+Fore.YELLOW).lower())
        _set1_ = _set_.split(' ')
        # Input for info show

    except KeyboardInterrupt:
        Exit._ret_()
    try:
        if (_set_ == '1') or ('-i' in _set1_) or ('-info' in _set1_) or ('information' in _set1_): # Menu 2 .. info bit ..
            os.system('clear')
            header.baner()
            time.sleep(0.1)
            infobit.info_bit()
            time.sleep(0.1)
            try:
                _num_ = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Information'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                _num1_ = _num_.split(' ')

                if ('-h' in _num1_) or ('-help' in _num1_) or ('help' in _num1_):
                    hl._start_()
                    time.sleep(0.1)
                    print(Fore.LIGHTBLUE_EX+"\nPress [Enter] for Back to menu...")
                    hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Guid'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())

                if (_num_ == '1') or ('-d' in _num1_)  or ('$' in _set1_) or ('-$' in _set1_) or ('dollar' in _num1_):
                    xd = ['-t']
                    while ('-t' in xd) or ('try' in xd):
                        dollar._start_()
                        print('\nPlease Waiting... \n')
                        change_doll = get_doll._start_()
                        typ = str(type(change_doll))

                        if typ == '<class \'str\'>' :
                            if change_doll == 'check':
                                print(Fore.RED+'Please Check a Connection... \n')
                                break
                        elif typ == '<class \'int\'>' :
                            if change_doll !=200:
                                er = change_doll
                                print(Fore.RED+'Humm I can not Connect      ERROR[%i] \n' % (er))
                                time.sleep(3)
                                break

                        elif typ == '<class \'list\'>' :
                            d = str(change_doll[0].replace('$', ''))
                            r1 = int(change_doll[1].replace(',', ''))

                            print(Fore.LIGHTYELLOW_EX+"\033[05m[1]\033[25m",Fore.LIGHTGREEN_EX+'Bitcoin is currently priced   ',Fore.LIGHTCYAN_EX+d,"$ \n")
                            print(Fore.LIGHTYELLOW_EX+"\033[05m[2]\033[25m",Fore.LIGHTGREEN_EX+'Dollar\'s price in Iran ^Rial^ ',Fore.LIGHTCYAN_EX+str(r1),"\n")
                            print(Fore.LIGHTBLUE_EX+"\nPress [Enter] for Back to menu...")
                            hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Information/bit_dolarr'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                            xd = hlp.split(' ')                
                if (_num_ == '2') or ('-r' in _num1_) or ('-rial' in _num1_) or ('rial' in _num1_): # 
                    xr = ['-t']
                    while ('-t' in xr) or ('try' in xr):
                        rial._start_()
                        print('\nPlease Waiting... \n')
                        change_rial = get_riall._start_()
                        typ = str(type(change_rial))
                        if typ == '<class \'str\'>' :
                            if change_rial == 'check':
                                print(Fore.RED+'Please Check a Connection... \n')
                                break
                        elif typ == '<class \'int\'>' :
                            if change_rial !=200:
                                er = change_rial
                                print(Fore.RED+'Humm I can not Connect      ERROR[%i] \n' % (er))
                                time.sleep(3)
                                break

                        elif typ == '<class \'list\'>' :
                            d2 = int(str(change_rial[0]).replace(',', ''))
                            r2 = int(str(change_rial[1]).replace(',', ''))
                            print(Fore.LIGHTYELLOW_EX+"\033[05m[1]\033[25m",Fore.LIGHTGREEN_EX+'Bitcoin is currently priced   ',Fore.LIGHTCYAN_EX+str(d2),'Toman',"\n")
                            print(Fore.LIGHTYELLOW_EX+"\033[05m[2]\033[25m",Fore.LIGHTGREEN_EX+'Dollar\'s price in Iran ^Rial^ ',Fore.LIGHTCYAN_EX+str(r2),"\n")
                            print(Fore.LIGHTBLUE_EX+"\nPress [Enter] for Back to menu... \n")
                            hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Information/bit_rial'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                            xd = hlp.split(' ')
                if (_num_ == '3') or ('-p' in _num1_) or ('-plt' in _num1_) or ('plot' in _num1_) or ('chart' in _num1_):
                    xc = ['-t']
                    while ('-t' in xc) or ('try' in xc):
                        chart._start_()
                        print('\nPlease Waiting... \n')
                        #charts._start_init()
                        chart_chang = charts._start_init()
                        typ =str(type(chart_chang))

                        if typ == '<class \'str\'>' :
                            if chart_chang == 'check':
                                print(Fore.RED+'Please Check a Connection... \n')
                                break

                        elif typ == '<class \'int\'>' :
                            if chart_chang !=200:
                                er = chart_chang
                                print(Fore.RED+'Humm I can not Connect      ERROR[%i] \n' % (er))
                                time.sleep(3)
                                break
                        print(Fore.LIGHTBLUE_EX+"\nPress [Enter] for Back to menu... \n")
                        hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Information/bit_chart'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                        xc = hlp.split(' ')                       
                if (_num_ == '4') or ('-c' in _num1_) or ('-curr' in _num1_) or ('currency' in _num1_) or ('currency available' in _num1_):
                    xcr = ['-t']
                    while ('-t' in xcr) or ('try' in xcr):
                        cur._start_()
                        print('\nPlease Waiting... \n')
                        change_cur = get_currenc._start_init()
                        typ = str(type(change_cur))
                        if typ == '<class \'str\'>' :
                            time.sleep(3)
                            if change_cur == 'check':
                                print(Fore.RED+'Please Check a Connection... \n')
                                break

                        elif typ == '<class \'int\'>' :
                            if change_cur !=200:
                                er = change_cur
                                print(Fore.RED+'Humm I can not Connect      ERROR[%i] \n' % (er))
                                time.sleep(3)
                                break

                        elif typ == '<class \'list\'>' :
                            d3 = str(change_cur[0]).replace(',', '')
                            r3 = int(str(change_cur[1]).replace(',', ''))

                            print(Fore.LIGHTYELLOW_EX+"\033[05m[1]\033[25m",Fore.LIGHTGREEN_EX+'Bitcoin is currently priced   ',Fore.LIGHTCYAN_EX+str(d3),'Million BTC',"\n")
                            print(Fore.LIGHTYELLOW_EX+"\033[05m[2]\033[25m",Fore.LIGHTGREEN_EX+'Dollar\'s price in Iran ^Rial^ ',Fore.LIGHTCYAN_EX+str(r3),"\n")
                            print(Fore.LIGHTBLUE_EX+"\nPress [Enter] for Back to menu... \n")
                            hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Information/bit_currency'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                            xcr = hlp.split(' ')
                if (_num_ == '6') or ('-b' in _num1_) or ('-back' in _num1_) or ('menu' in _num1_):
                    os.system('clear')
                    print('Back to menu Bit Coin')
                    time.sleep(1)
                if (_num_ == '5') or ('-q' in _num1_) or ('-quit' in _num1_) or ('exit' in _num1_):
                    os.system('clear')
                    Ex._start_()
                    time.sleep(1)
                    break
        
            except:
                os.system('clear')
                print(Fore.LIGHTRED_EX+'Be sure to share this issue with the developer of this program')
                print(Fore.LIGHTYELLOW_EX+'ysnblackhat@gmail.com')
                break
        elif (_set_ == '2') or ('-g' in _set1_) or ('-change' in _set1_) or ('changer' in _set1_) or ('changer' in _set1_) or ('exchang' in _set1_): # Menu 3 .. Change bit ..
            os.system('clear')
            header.baner()
            time.sleep(0.1)
            info_change.info_change()
            time.sleep(0.1)
            try:
                _num_ = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Changer'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                _num1_ = _num_.split(' ')

                if (_num_ == '1') or('-x' in _num1_) or ('-exchang' in _num1_) or ('exchange' in _num1_):
                    xe = ['-t']
                    while ('-t' in xe) or ('try' in xe):
                        exchanger._init_()
                        time.sleep(0.1)
                        os.system('clear')
                        exchanger._init_()
                        tp = exchang._init_()

                        if ('USD' in tp) and ('IRT' in tp):
                            print(Fore.RED+'Please do not use two government currencies at the same time')
                        else: 
                            os.system('clear')
                            exchanger._init_()
                            time.sleep(0.1)
                            print(Fore.LIGHTYELLOW_EX+'Response request : ',Fore.LIGHTRED_EX+tp[5])
                            print(Fore.LIGHTYELLOW_EX+'the Value of Use : ',Fore.LIGHTRED_EX+tp[0])
                            print('')
                            print(Fore.LIGHTGREEN_EX+'Orige : ',Fore.LIGHTCYAN_EX+tp[1])
                            print(Fore.LIGHTGREEN_EX+'Convert To')
                            print(Fore.LIGHTGREEN_EX+'Destination Value of Use :',Fore.LIGHTCYAN_EX+tp[2])
                            print('')
                            print(Fore.LIGHTGREEN_EX+'|','Dollar Rate :',Fore.LIGHTCYAN_EX+tp[3])
                            print('|')
                            print('|')
                            tp1 = str(tp[4]).split(' ')
                            print(Fore.LIGHTGREEN_EX+'|',tp1[0],Fore.LIGHTCYAN_EX+tp1[1],Fore.LIGHTGREEN_EX+tp1[2])
                        print(Fore.LIGHTCYAN_EX+"\nPress [Enter] for Back to menu...")
                        hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Changer/bit_exchange'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                        xe = hlp.split(' ')
                if (_num_ == '2') or ('-l' in _num1_) or ('-list' in _num1_) or ('list' in _num1_) or ('rate' in _num1_):
                    xl = ['-t']
                    while ('-t' in xl) or ('try' in xl): # try
                        xl = []
                        rate_list._getdes_()
                        time.sleep(0.1)
                        rate_list._pritnt_()

                        print(Fore.LIGHTCYAN_EX+"\nPress [Enter] for Back to menu...")
                        hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Changer/bit_list'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
                        xl = hlp.split(' ')
                if (_num_ == '3') or ('-q' in _num1_) or ('-quit' in _num1_) or ('exit' in _num1_):
                    os.system('clear')
                    Ex._start_()
                    time.sleep(1)
                    break
                if (_num_ == '4') or ('-b' in _num1_) or ('-back' in _num1_) or ('menu' in _num1_):
                    os.system('clear')
                    print('Back to menu Bit Coin')
                    time.sleep(1)

            except:
                os.system('clear')
                print(Fore.LIGHTRED_EX+'Be sure to share this issue with the developer of this program')
                print(Fore.LIGHTYELLOW_EX+'ysnblackhat@gmail.com')
                break
        elif (_set_ == '3') or ('-h' in _set1_) or ('-help' in _set1_) or ('help' in _set1_): # Menu 3 .. Help bit ..
            hl._start_()
            time.sleep(0.1)
            print(Fore.LIGHTBLUE_EX+"\nPress [Enter] for Back to menu...")
            hlp = str(input(Fore.LIGHTYELLOW_EX+'┌─['+Fore.LIGHTBLUE_EX+'Bitcoin% '+Fore.LIGHTGREEN_EX+'blackhat~@ '+Fore.LIGHTMAGENTA_EX+'Home/bit_Guid'+Fore.LIGHTYELLOW_EX+']\n└──╼'+Fore.LIGHTWHITE_EX+'\033[05m 卐 \033[25m' +Fore.YELLOW).lower())
        elif (_set_ == '4') or ('-q' in _set1_) or ('-quit' in _set1_) or ('exit' in _set1_) or ('quit' in _set1_): # Menu 4 .. Exit bit ..
            os.system('clear')
            Exit._ret_()

        else: 
            os.system("clear")
            print(Fore.LIGHTRED_EX+"Please Enter a Valid Plane")
            sys.exit()
            
    except KeyboardInterrupt:
        Exit._ret_()
    except:
        os.system("clear")
        sys.exit()
