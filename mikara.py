#!/usr/bin/env python3

from mods.args import *
from mods.colors import *
from mods.functions import *
import threading
import os


def main1():
    
    get_profile()
    
    print(color.BLUE+"\nGenerating simple wordlist..."+color.END)
    
    # Simple
    set_0()
    set_00()
    set_000()
    
    with open(wordlist, 'w') as w:
        for x in set(global_list):
            w.write(x+"\n")
            
def main2():
    
    get_profile()
    
    print(color.BLUE+"\nGenerating moderate wordlist..."+color.END)
    
    # Simple
    set_0()
    set_00()
    set_000()
    
    # Moderate
    set_1()
    set_11()
    set_111()
        
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            w.write(x+"\n")
            
def main3():
    
    get_profile()
    
    print(color.BLUE+"\nGenerating complex wordlist..."+color.END)
    
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
    
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            w.write(x+"\n")
            
def main4():
    
    get_profile()
    
    print(color.BLUE+"\nGenerating ultra complex wordlist..."+color.END)

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
    
    # Ultra Complex
    set_3()
    set_33()
    set_333()
    
    
    
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            w.write(x+"\n")
            
    

if __name__ == '__main__':
    if args.output != None and args.type == 'simple':
        print(banner)
        main1()
        print(color.GREEN+"\n[+] Simple wordlist generated and saved to "+os.path.abspath(wordlist)+color.END)
        
    elif args.output != None and args.type == 'moderate':
        print(banner)
        main2()
        print(color.GREEN+"\n[+] Moderate wordlist generated and saved to "+os.path.abspath(wordlist)+color.END)
        
    elif args.output != None and args.type == 'complex':
        print(banner)
        main3()
        print(color.GREEN+"\n[+] Complex wordlist generated and saved to "+os.path.abspath(wordlist)+color.END)
        
    elif args.output != None and args.type == 'ultracomplex':
        print(banner)
        main4()
        print(color.GREEN+"\n[+] Ultra complex wordlist generated and saved to "+os.path.abspath(wordlist)+color.END)
        
    else:
        parser.error("A required argument is missing")        