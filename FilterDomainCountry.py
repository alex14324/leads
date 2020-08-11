from datetime import *
import os
from platform import system
from colorama import Fore								
from colorama import Style
from colorama import init
init(autoreset=True)
init(autoreset=True)
fr  =   Fore.RED
fc  =   Fore.CYAN											
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
os.system('title Filter Domain\Country by MAD-HACKER')
def clear():
    if system()=='Linux':
        os.system('clear')
    elif system()=='Windows':
        os.system('cls')
today = datetime.today()
month = today.strftime('%B' + ' /')
day = today.strftime('%d' + ' /')
year = today.strftime('%Y')
print("{}{}\n\t\tDatetime Today : "+"[ " + (day) + " " + (month) + " " + (year)+" ]").format(fc,sb)
banner='''{}{}\t

                       ++++++++++++++++++++++++++++++++++

                        Filter Domain / Country

                             Re-coded by : MAD-HACKER
					Telegram: @madhacker
							 
                                 
                       ++++++++++++++++++++++++++++++++++

'''.format(fy,sb)
print(banner)
siyass='''\n\n{}{}


                 \ \/ /\ \ / / \ | _ \| \ | |_ _| \ | |/ ___|
                  \ / \ \ /\ / / _ \ | |_) | \| || || \| | | _ 
                   / \ \ V V / ___ \| _ <| |\ || || |\ | |_| |
                 /_/\_\ \_/\_/_/ \_\_| \_\_| \_|___|_| \_|\____|
                          MAD-HACKER | t.me/madhacker



'''.format(fc,sb)
print('{}{}\n\t\t[1] Country Filtre (exp : ca net com us)').format(fg,sb)
print('{}{}\n\t\t[2] Domain Filtre (exp : hotmail gmail aol yahoo)').format(fg,sb)
filt = raw_input(("{}{}\n\n\tWhat You Wana Choose ? ==> ").format(fr,sb))
def filters():
    list = raw_input(('{}{}\n\tEnter Name Of Mailist For Filter It ==> ').format(fy,sb))
    type = raw_input(('{}{}\n\t\tEnter Type Of Country You Wanna Filter (exp : ca com net) ==> ').format(fc,sb))
    clear()
    print(siyass)
    file = open(list).readlines()
    if (len(file) > 0):
      for ip in file:
        sites = ip.rstrip()
        type2 = '.' + (type)
        if type2 in sites:
            print ('{}{}Resul Will Be Save To Result.txt :D\t\t ==> '+(sites)).format(fg,sb)
            f = open('Result.txt', 'a')
            f.write(sites) 
            f.write('\n')
        else:
            pass
	
def filters2():
    list = raw_input(('{}{}\n\tEnter List Of Email For Filter It ==> ').format(fy,sb))
    type = raw_input(('{}{}\n\t\tEnter Type Of Domain You Wanna Filter (exp : gmail aol yahoo) ==> ').format(fc,sb))
    clear()
    print(siyass)
    file = open(list).readlines()
    if (len(file) > 0):
      for ip in file:
        sites = ip.rstrip()
        type2 = (type)
        if type2 in sites:
            print ('{}{}Result Will Be Save To Result2.txt :D\t\t ==> '+ (sites)).format(fg,sb)
            f = open('Result2.txt', 'a')
            f.write(sites) 
            f.write('\n')
if filt =='1':
    filters()
elif filt == '2':
    filters2()
else:
    pass
    
