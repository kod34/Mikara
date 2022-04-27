#!/usr/bin/env python3

from mods.args import *
from mods.colors import *
from mods.functions import *
import threading
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
            print('Progress: '+color.YELLOW+'%d\r'%set(global_list).index(x)*100/len(set(global_list))+color.END, end="")
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
    
    print(color.GREEN+"[+] Wordlist successfully generated"+color.END)
        
    print(color.BLUE+"[~] Storing in file..."+color.END)
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            print('Progress: '+color.YELLOW+'%d\r'%set(global_list+m_global_list).index(x)*100/len(set(global_list+m_global_list))+color.END, end="")
            w.write(x+"\n")
            
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
    
    print(color.GREEN+"[+] Wordlist successfully generated"+color.END)
    
    print(color.BLUE+"[~] Storing in file..."+color.END)
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            print('Progress: '+color.YELLOW+'%d\r'%set(global_list+m_global_list).index(x)*100/len(set(global_list+m_global_list))+color.END, end="")
            w.write(x+"\n")
            
def main4():
    
    get_profile()
    
    print(color.BLUE+"\n[~] Generating ultra complex wordlist..."+color.END)

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
    
    print(color.GREEN+"[+] Wordlist successfully generated"+color.END)
    
    print(color.BLUE+"[~] Storing in file..."+color.END)
    with open(wordlist, 'w') as w:
        for x in set(global_list+m_global_list):
            print('Progress: '+color.YELLOW+'%s\r'%x+color.END, end="")
            w.write(x+"\n")
            
    

if __name__ == '__main__':
    if args.output != None and args.type == 'simple':
        print(banner)
        main1()
        print(color.GREEN+"[+] Wordlist saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        
    elif args.output != None and args.type == 'moderate':
        print(banner)
        main2()
        print(color.GREEN+"[+] Wordlist saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        
    elif args.output != None and args.type == 'complex':
        print(banner)
        main3()
        print(color.GREEN+"[+] Wordlist saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        
    elif args.output != None and args.type == 'ultracomplex':
        print(banner)
        main4()
        print(color.GREEN+"[+] Wordlist saved to "+color.YELLOW+os.path.abspath(wordlist)+color.END+color.END)
        
    else:
        parser.error("A required argument is missing")        