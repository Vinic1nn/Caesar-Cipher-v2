#!/usr/bin/env python3 

from colorama import Back, Fore, Style
print(Fore.GREEN + Back.RED + ' CAESAR CIPHER 2.0 '+ Style.RESET_ALL)

def textDeslocation(text, dslc):
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        code = ord(char) + dslc
        if char.islower():
            if code > ord('z'):
                rest = (code - ord('z')) % 26
                code = ord('a') + rest - 1
        else:
            if code > ord('Z'):
                rest = (code - ord('Z')) % 26
                code = ord('A') + rest - 1
        cipher += chr(code)
    print(Style.BRIGHT + Fore.WHITE + Back.GREEN + " " + cipher + " " + Style.RESET_ALL)   
        
def init():
    text = input('Type a text to encrypt: ').strip()
    dslc = int(input('Type a number to deslocation within 1 and 25: '))
    while dslc < 1 or dslc > 25:
        dslc = int(input('Type a number to dislocation within 1 and 25: '))
    textDeslocation(text, dslc)
 
if __name__ == "__main__":
    print("Run main")
    
