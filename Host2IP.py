# Imports
from socket import gethostbyname
from colorama import Fore, init
from os import name, system
from time import sleep

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

    SCRIPT_VERSION = "1.0"
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
           \n\n"""
    # clean-up Command-Line
    system("cls" if name == "nt" else "clear")
    print(LIGHTRED + TEXT)


def start():
    """
        Run the main menu of the script
        :return:
        """
    printer = Tprint()
    # Main loop
    while True:
        banner()
        try:
            # Get host name from user
            HOST = input(GREEN + " [+]" + LIGHTYELLOW + " Please enter the host name > " + LIGHTWHITE + "")
            # Remove 'http://' and 'https://' in host name
            if "http://" in HOST or "https://" in HOST:
                HOST.replace("http://", "").replace("https://", "")
            # Show error if 'HOST' is empty
            if HOST == "":
                printer.out(RED + " [-] Error : Please enter a host name !!!")
            # break the loop if user entered 'exit'
            if HOST.lower() == "exit":
                break
            else:
                # get ip address of host name using socket library
                IP = gethostbyname(HOST)
                print("\n")
                printer.out(LIGHTRED + " [+]" + LIGHTCYAN + " Finding IP address ...")
                sleep(3)
                printer.out(LIGHTGREEN + " [+]" + LIGHTCYAN + " Found IP address of " + LIGHTWHITE
                            + f"[{HOST}]" + LIGHTCYAN + " |" + LIGHTWHITE + f" {IP}")
                sleep(3)
                input(LIGHTWHITE + "\n\n [+] Press [ENTER] to try again... ")
        except Exception as e:
            if "getaddrinfo failed" and "11001" in str(e):
                print("\n" + RED + "[-] Error : Please enter a valid host name ! (e.g github.com)")
            else:
                # print general error
                print("\n" + RED + f" [-] Error : {e}")
            input(LIGHTWHITE + "\n\n [+] Press [ENTER] to try again... ")
        except KeyboardInterrupt:
            # break the loop if user pressed 'Ctrl+C'
            system("cls" if name == "nt" else "clear")
            break


if __name__ == "__main__":
    start()
