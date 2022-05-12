#!/usr/bin/env python3

from mods.args import *
from mods.colors import *
from mods.functions import *
import os

def main1():
    
    get_profile()
    
    print(color.BLUE+"\n[~] Generating simple wordlist..."+color.END)
    
    # Simple
    set_0()
    set_00()
    set_000()
    
    print(color.GREEN+"[+] Wordlist successfully generated"+color.END)
    
    print(color.BLUE+"[~] Storing in file..."+color.END)
    with open(wordlist, 'w') as w:
        for x in set(global_list):
            print("Progress: "+color.YELLOW+x+color.END, end="\r")
            w.write(x+"\n")
            
def main2():
    
    get_profile()
    
    print(color.BLUE+"\n[~] Generating moderate wordlist..."+color.END)
    
    # Simple
    set_0()
    set_00()
    set_000()
    
    # Moderate
    set_1()
    set_11()
    set_111()
    
            
def main3():
    
    get_profile()
    
    print(color.BLUE+"\n[~] Generating complex wordlist..."+color.END)
    
    # Simple
    set_0()
    set_00()
    set_000()
    
    # Moderate
    set_1()
    set_11()
    set_111()
    
    # Complex
    set_2()
    set_22()
    set_222()
            
def main4():
    
    get_profile()
    
    print(color.BLUE+"\n[~] Generating impossible wordlist..."+color.END)

    # Simple
    set_0()
    set_00()
    set_000()
    
    # Moderate
    set_1()
    set_11()
    set_111()
    
    # Complex
    set_2()
    set_22()
    set_222()
    
    # impossible
    set_3()
    set_33()
    set_333()
    
def main5():
    get_profile()
    
    print(color.BLUE+"\n[~] Generating ridiculous wordlist..."+color.END)

    # Simple
    set_0()
    set_00()
    set_000()
    
    # Moderate
    set_1()
    set_11()
    set_111()
    
    # Complex
    set_2()
    set_22()
    set_222()
    
    # impossible
    set_3()
    set_33()
    set_333()
    
    # ridiculous
    set_4()

            
def last_touch():
    print(color.GREEN+"[+] Wordlist successfully generated"+color.END)
    
    print(color.BLUE+"[~] Storing in file..."+color.END)
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            print("Progress: "+color.YELLOW+x+color.END, end="\r")
            w.write(x+"\n")
            
try:
    if __name__ == '__main__':
        if args.output != None and args.type == 'simple' and args.size != None and args.size != None:
            try:int(args.size)
            except:sys.exit(color.RED+"[-] Size must be an integer"+color.END)
            print(banner)
            main1()
            print(color.GREEN+"[+] "+color.YELLOW+str(len(set(global_list)))+color.GREEN+" words saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        elif args.output != None and args.type == 'moderate' and args.size != None:
            try:int(args.size)
            except:sys.exit(color.RED+"[-] Size must be an integer"+color.END)
            print(banner)
            main2()
            last_touch()
            print(color.GREEN+"[+] "+color.YELLOW+str(len(set(global_list+m_global_list)))+color.GREEN+" words saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        elif args.output != None and args.type == 'complex' and args.size != None :
            try:int(args.size)
            except:sys.exit(color.RED+"[-] Size must be an integer"+color.END)
            print(banner)
            main3()
            last_touch()
            print(color.GREEN+"[+] "+color.YELLOW+str(len(set(global_list+m_global_list)))+color.GREEN+" words saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        elif args.output != None and args.type == 'impossible' and args.size != None:
            try:int(args.size)
            except:sys.exit(color.RED+"[-] Size must be an integer"+color.END)
            print(banner)
            main4()
            last_touch()
            print(color.GREEN+"[+] "+color.YELLOW+str(len(set(global_list+m_global_list)))+color.GREEN+" words saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        elif args.output != None and args.type == 'ridiculous' and args.size != None:
            try:int(args.size)
            except:sys.exit(color.RED+"[-] Size must be an integer"+color.END)
            print(banner)
            main5()
            last_touch()
            print(color.GREEN+"[+] "+color.YELLOW+str(len(set(global_list+m_global_list)))+color.GREEN+" words saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        else:
            parser.error(color.RED+"A required argument is missing"+color.END)  
except KeyboardInterrupt:
    sys.exit(color.RED+"[-] Keyboard Interrupt"+color.END)