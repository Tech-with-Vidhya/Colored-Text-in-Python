import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.GREEN + 'Green Text')
print(Back.BLUE + 'Yellow Back Text')
print(Style.BRIGHT + 'Bright Text')
print(Fore.BLUE + Back.LIGHTGREEN_EX + Style.DIM + 'THIS IS TECH WITH VIDHYA')
print(f"{Fore.GREEN}C{Fore.BLUE}O{Fore.YELLOW}L{Fore.MAGENTA}O{Fore.CYAN}R{Fore.RED}S")
print(f"{Fore.RED}{Back.YELLOW}{Style.BRIGHT}TECH WITH VIDHYA")
print(f"{Fore.BLUE}THIS {Fore.MAGENTA}IS {Fore.RED}TECH {Fore.CYAN}WITH {Fore.BLUE}VIDHYA{Fore.YELLOW}.....")
print(f"{Fore.GREEN}{Back.CYAN}{Style.BRIGHT}TECH", f"{Fore.LIGHTWHITE_EX}{Back.RED}{Style.DIM}WITH", f"{Fore.LIGHTYELLOW_EX}{Back.MAGENTA}{Style.NORMAL}VIDHYA")


'''
Fore: BLACK, RED, GREEN, LIGHTGREEN_EX, YELLOW, LIGHTYELLOW_EX, BLUE, MAGENTA, CYAN, WHITE, LIGHTWHITE_EX, RESET.
Back: BLACK, RED, GREEN, LIGHTGREEN_EX, YELLOW, LIGHTYELLOW_EX, BLUE, MAGENTA, CYAN, WHITE, LIGHTWHITE_EX, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''