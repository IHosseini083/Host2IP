# Imports
from os import getcwd, getlogin, name, system
from socket import gethostbyname
from time import sleep

from colorama import Fore, init
from requests import get

init()
# Colors
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
WHITE = Fore.WHITE
LIGHTGREEN = Fore.LIGHTGREEN_EX
LIGHTRED = Fore.LIGHTRED_EX
LIGHTWHITE = Fore.LIGHTWHITE_EX
LIGHTYELLOW = Fore.LIGHTYELLOW_EX
LIGHTCYAN = Fore.LIGHTCYAN_EX


class Tprint:
    def __init__(self):
        self.max_len = 0

    def out(self, text):
        if len(text) > self.max_len:
            self.max_len = len(text)
        else:
            text += (" " * (self.max_len - len(text)))
        print(text, end='\r')


def banner():
    """
        contains the script banner with RED color
        :return:
        """

    SCRIPT_VERSION = "1.1"
    TELEGRAM_CHANNEL = "Distrotv"

    TEXT = f"""

        _               _   ___  _       
       | |             | | |__ \(_)      
       | |__   ___  ___| |_   ) |_ _ __  
       | '_ \ / _ \/ __| __| / /| | '_ \ 
       | | | | (_) \__ \ |_ / /_| | |_) |
       |_| |_|\___/|___/\__|____|_| .__/ 
                                  | |    
                                  |_|
                                      
        Version : {SCRIPT_VERSION} ~ TelegramChannel : {TELEGRAM_CHANNEL} 

 + =============================================== +  
   
 [!] Press Ctrl+C to exit or enter 'q'                                       
           """
    # clean-up Command-Line
    system("cls" if name == "nt" else "clear")
    print(LIGHTRED + TEXT)


def start():
    """
        Run the main menu of the script
        :return:
        """
    printer = Tprint()
    # get current username of pc
    USERPROFILE = getlogin()
    # current Drive that script is running on
    C_DRIVE = getcwd().split("\\")[-1].replace(":", "")
    # Main loop
    while True:
        banner()
        try:
            print("\n" + LIGHTYELLOW + " [!] Please enter the host name.")
            # Get host name from user
            HOST = input(
                "\n" + LIGHTGREEN + " ┌─[" + LIGHTCYAN + f"{USERPROFILE}" + LIGHTWHITE + "@" + LIGHTCYAN + "Host2IP" + LIGHTGREEN + "]─[" + LIGHTCYAN + f"~/{C_DRIVE}" + LIGHTGREEN + "]" + """
 └──╼/# """ + LIGHTWHITE + "")
            # Remove 'http://' and 'https://' in host name
            if "http://" in HOST or "https://" in HOST:
                HOST.replace("http://", "").replace("https://", "")
            else:
                pass
            # Remove "www." from host name
            if "www." in HOST:
                HOST.replace("www.", "")
            else:
                pass
            # Show error if 'HOST' is empty
            if len(HOST) == 0:
                printer.out(RED + " [-] Error : Please enter a host name !!!")
            else:
                pass
            # break the loop if user entered 'exit'
            if HOST.lower() == "q":
                system("cls" if name == "nt" else "clear")
                break
            else:
                # get ip address of host name using socket library
                IP = gethostbyname(HOST)
                # get data about IP addr
                DATA = get(f"http://ipinfo.io/{IP}/json").json()
                try:
                    # country of IP
                    COUNTRY = DATA["country"]
                except:
                    COUNTRY = "Unknown Country"
                try:
                    # region of IP
                    REGION = DATA["region"]
                except:
                    REGION = "Unknown Region"
                try:
                    # server of IP
                    SERVER = DATA["org"]
                except:
                    SERVER = "Unknown Server"
                print("\n")
                printer.out(LIGHTRED + " [+]" + LIGHTCYAN + " Retrieving IP address ...")
                sleep(3)
                printer.out(LIGHTGREEN + " [+] " + LIGHTWHITE
                            + f"{HOST}" + LIGHTCYAN + " |" + LIGHTWHITE + f" {IP} " + LIGHTCYAN + "| " +
                            LIGHTWHITE + f"{COUNTRY}" + LIGHTCYAN + " - " + LIGHTWHITE + f"{REGION}" +
                            LIGHTCYAN + " | " + LIGHTWHITE + f"{SERVER}")
                sleep(2)
                print("\n\n")
                input(LIGHTWHITE + " [+] Press [" + RED + "ENTER" + LIGHTWHITE + "] to try again... ")
        except Exception as e:
            # this error occurred because of connection issues or bad entry
            if "getaddrinfo failed" and "11001" in str(e):
                print("\n")
                print(LIGHTRED + " [-] " + LIGHTYELLOW + "Error : Check your internet connection\n\n or check if you "
                                                         "entered a valid host name ! (e.g github.com)")
                sleep(2)
                print("\n")
            else:
                print("\n")
                # print general error
                print(LIGHTRED + " [-]" + LIGHTYELLOW + f" Error : {e}")
                sleep(2)
                print("\n\n")
            input(LIGHTWHITE + " [+] Press [" + RED + "ENTER" + LIGHTWHITE + "] to try again... ")
        except KeyboardInterrupt:
            # break the loop if user pressed 'Ctrl+C'
            system("cls" if name == "nt" else "clear")
            break


if __name__ == "__main__":
    start()
