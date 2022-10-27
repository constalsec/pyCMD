# made by constalsec - cmd bypasser in python3.10

from os import system, name, getlogin
from colorama import Fore, Back, init
from socket import gethostname, gethostbyname

scheme1 = Fore.GREEN
scheme2 = Fore.LIGHTMAGENTA_EX

hostname = gethostname()
address = gethostbyname(hostname)

ascii = """
--------------------------------------------------------------                                                              

                       .g8\"\"\"bgd `7MMM.     ,MMF'`7MM\"\"\"Yb.   
                     .dP'     `M   MMMb    dPMM    MM    `Yb. 
`7MMpdMAo.`7M'   `MF'dM'       `   M YM   ,M MM    MM     `Mb 
  MM   `Wb  VA   ,V  MM            M  Mb  M' MM    MM      MM 
  MM    M8   VA ,V   MM.           M  YM.P'  MM    MM     ,MP 
  MM   ,AP    VVV    `Mb.     ,'   M  `YM'   MM    MM    ,dP' 
  MMbmmd'     ,V       `"bmmmd'  .JML. `'  .JMML..JMMmmmdP'   
  MM         ,V                                               
.JMML.    OOb\"                                                
 
 
--------------------------------------------------------------
 """


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def onstart():
    clear()
    init()
    print(Fore.GREEN+ascii)
    print(Fore.LIGHTCYAN_EX+"")


def execmd():
    choice = input(str(getlogin())+"@"+"pyCMD > ")
    if choice == "cls":
        onstart()
    else:
        system(choice)


onstart()

while True:
    execmd()
