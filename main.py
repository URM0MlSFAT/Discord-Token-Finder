# coding: utf-8
#!/usr/bin/env python


#<--------------Imports Start & Loading-------------->
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os

os.system("title Tokyo - Loading...")
print(f"""
{Fore.MAGENTA}
                                                                         mm  
     @@@**@@**@@@       @@                                               @@  
     @*   @@   *@       @@                                                   
          @@          @@@@@@       m@*@@m       *@@*    m@    *@@*     *@@@  
          !@            @@        @@   @@         @@   m@@@   m@         @@  
          !@            @@         m@@@!@          @@ m@  @@ m@          !@  
          !@            @!        @!   !@           @@@    @!!           !@  
          !@            !!         !!!!:!           !@!!   !:!           !!  
          !!            !!        !!   :!           !!!    !:!           !!  
        : :!::          ::: :     :!: : !:           :      :          : : : 

                                       {Fore.WHITE}          Loading...
""")
print(f"{Fore.MAGENTA}")
progressbar = tqdm([2,4,6,8,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')

import base64, pyperclip
#<--------------Imports End-------------->

os.system("title Ttawi - Ready")
os.system("cls")
print(f"""
{Fore.MAGENTA}
                                                                         mm  
     @@@**@@**@@@       @@                                               @@  
     @*   @@   *@       @@                                                   
          @@          @@@@@@       m@*@@m       *@@*    m@    *@@*     *@@@  
          !@            @@        @@   @@         @@   m@@@   m@         @@  
          !@            @@         m@@@!@          @@ m@  @@ m@          !@  
          !@            @!        @!   !@           @@@    @!!           !@  
          !@            !!         !!!!:!           !@!!   !:!           !!  
          !!            !!        !!   :!           !!!    !:!           !!  
        : :!::          ::: :     :!: : !:           :      :          : : : 

                                    {Fore.WHITE}        Input the User ID




""")

id = " root" + Fore.WHITE+"@" + Fore.MAGENTA+"Ttawi" + Fore.WHITE+":" + Fore.CYAN+"~" + Fore.WHITE+"dox" + Fore.WHITE+" ")

)
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Valid ID!')
    data = f'{id}'
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] {encodedStr}')
    print('')
    copy = input(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Do you want copy this text? (y/n){Fore.WHITE} ')

    if copy == "y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Text Copied!')

    if copy == "Y":
        pyperclip.copy(encodedStr)
        print('')
        print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Text Copied!')

    else:
        print('')
        print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to Exit')
        input()

except ValueError:
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Invalid ID!')
    print('')
    print(f'{Fore.MAGENTA} [{Fore.WHITE}+{Fore.MAGENTA}] Press enter to Exit')
    input()
