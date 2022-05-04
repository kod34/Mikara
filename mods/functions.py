from curses.ascii import isdigit
from itertools import *
from datetime import datetime
from mods.args import *
from mods.colors import *


common_first = [ '!', '@', '*', '$', '&', '%', '123', '456', '789', '000', '321', '987', '654', '321'] + list(range(0,99))
common_middle = ['_', '.', '-', '!', '@', '*', '$', '?', '&', '%', '123', '456', '789', '000', '321', '987', '654', '321'] + list(range(0,99))
common_last = ['.', '!', '@', '*', '$', '?', '&', '%', '123', '456', '789', '000', '321', '987', '654', '321'] + list(range(0,99))

global_list = []
m_global_list = []

def get_profile():
    global profile
    profile = {}
    birthday_stripped = []
    birthday = []
    res = False
    p = False
    
    # Get info
    fullname = input(color.YELLOW+"[*] Full Name: "+color.END).lower().split()
    nickname = input(color.YELLOW+"[*] Nickname: "+color.END).lower().split()
    
    ## Validate Birthday
    while (not res and len(birthday) != 0) or not p:
        birthday = input(color.YELLOW+"[*] Birthday(DD-MM-YYYY): "+color.END)
        p = True
        try:
            res = bool(datetime.strptime(birthday, '%d-%m-%Y'))
        except ValueError:
            res = False
            
    ## Add items to birthday
    if len(birthday) > 2:
        birthday = birthday.split('-')
        for x in birthday[:2]:
            birthday_stripped.append(x.lstrip('0'))
        if birthday_stripped[0] == birthday[0]:
            birthday_stripped.pop(0)
        if birthday_stripped[1] == birthday[1]:
            birthday_stripped.pop(1)
    
    year = input(color.YELLOW+"[*] Current year: "+color.END).lower().split()
    pets = input(color.YELLOW+"[*] Pet Names: "+color.END).lower().split()
    mothername = input(color.YELLOW+"[*] Mother's Full Name: "+color.END).lower().split()
    fathername = input(color.YELLOW+"[*] Father's Full Name: "+color.END).lower().split()
    partnername = input(color.YELLOW+"[*] Partner's Full Name: "+color.END).lower().split()
    children = input(color.YELLOW+"[*] Chidren's First Names(ex: adam sara): "+color.END).lower().split()
    children_nick = input(color.YELLOW+"[*] Chidren's Nicknames: "+color.END).lower().split()
    
    ## for language and maybe stats on passwords
    country = input(color.YELLOW+"[*] Country Of Residence: "+color.END).lower().split()
    state = input(color.YELLOW+"[*] State Of Residence: "+color.END).lower().split()
    city = input(color.YELLOW+"[*] City Of Residence: "+color.END).lower().split()
    race = input(color.YELLOW+"[*] Race: ").lower().split()
    
    company = input(color.YELLOW+"[*] Company's Name: "+color.END).lower().split()
    interests = input(color.YELLOW+"[*] Interests(ex: football chess): "+color.END).lower().split()
    extra = input(color.YELLOW+"[*] Extra keywords(ex: nasa apple): "+color.END).lower().split()
        
    # Build profile
    profile['fullname'] = fullname
    profile['nickname'] = nickname
    profile['birthday'] = birthday
    profile['birthday_stripped'] = birthday_stripped
    profile['year'] = year
    profile['pets'] = pets
    profile['mothername'] = mothername
    profile['fathername'] = fathername
    profile['partnername'] = partnername
    profile['children'] = children
    profile['children_nick'] = children_nick
    profile['country'] = country
    profile['state'] = state
    profile['city'] = city
    profile['company'] = company
    profile['interests'] = interests
    profile['extra'] = extra
    
    return profile

def data_list():
    global l
    l = []
    for x in profile:
        for y in profile[x]:
            l.append(y)
    return set(l)
    

# Generate simple wordset with solo keys (ex: john\n smith\n football\n)
def set_0():
    for x in profile:
        if x != 'country' and x != 'company' and x != 'state' and x != 'city' and profile[x] != []:
            if len(profile[x]) > 1:
                word = ''.join(profile[x])
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(global_list))+color.END, end="\r")
                    global_list.append(word)
                for y in profile[x]:
                    word = str(y)
                    if len(word) >= int(size):
                        print("Progress: "+color.YELLOW+str(len(global_list))+color.END, end="\r")
                        global_list.append(word)
            else:
                try:
                    word = str(profile[x][0])
                except IndexError:
                    word = str(profile[x])
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(global_list))+color.END, end="\r")
                    global_list.append(word)
         
# Generate simple wordset with 2 mixed keys (ex: johnfootball\n john1990\n)
def set_00():
    a = permutations(data_list(),2)
    for c in list(a):
        word = c[0]+c[1]
        if len(word) >= int(size):
            print("Progress: "+color.YELLOW+str(len(global_list))+color.END, end="\r")
            global_list.append(word)
                    
# Generate simple wordset with 3 mixed keys (ex: johnfootball1990\n johnlinda2010\n)
def set_000():
    a = permutations(data_list(),3)
    for c in list(a):
        word = c[0]+c[1]+c[2]
        if len(word) >= int(size):
            print("Progress: "+color.YELLOW+str(len(global_list))+color.END, end="\r")
            global_list.append(word)
                
# Generate words beginning with common_first list
def set_1():
    notdigit = False
    for x in global_list:
        try:
            int(x)
            notdigit = False
        except:
            notdigit = True
        if notdigit:
            for c in common_first:
                word = str(c)+str(x)
                print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                m_global_list.append(word)
             
# Generate words with common_middle
def set_11():
    a = permutations(data_list(),2)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                word = str(c).join(x)
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word)
    a = permutations(data_list(),3)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                word = str(c).join(x)
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word)
                        
# Generate words with common_last
def set_111():
    notdigit = False
    for x in global_list:
        try:
            int(x)
            notdigit = False
        except:
            notdigit = True
        if notdigit:
            for c in common_last:
                word = str(x)+str(c)
                print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                m_global_list.append(word)             
                        
# Generate words mixed common_first common_last
def set_2():
    notdigit = False
    for x in global_list:
        try:
            int(x)
            notdigit = False
        except:
            notdigit = True
        if notdigit:
            for c in common_middle:
                word = str(c)+str(x)+str(c)
                print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                m_global_list.append(word) 
                
# Generate words mixed common_first common_middle
def set_22():
    a = permutations(data_list(),2)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                word = str(c)+str(c).join(x)
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word)
    a = permutations(data_list(),3)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                word = str(c)+str(c).join(x)
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word) 
                
# Generate words mixed common_middle common_last
def set_222():
    a = permutations(data_list(),2)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                word = str(c).join(x)+str(c)
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word)
    a = permutations(data_list(),3)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                word = str(c).join(x)+str(c)
                if len(word) >= int(size):
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word)
                
# Generate words mixed common_first common_last
def set_3():
    notdigit = False
    for x in global_list:
        try:
            int(x)
            notdigit = False
        except:
            notdigit = True
        if notdigit:
            for c in common_last:
                for g in common_first:
                    word = str(g)+str(x)+str(c)
                    print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                    m_global_list.append(word) 
                
# Generate words mixed common_first common_middle
def set_33():
    a = permutations(data_list(),2)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                for g in common_first:
                    word = str(g)+str(c).join(x)
                    if len(word) >= int(size):
                        print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                        m_global_list.append(word)
    a = permutations(data_list(),3)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                for g in common_first:
                    word = str(g)+str(c).join(x)
                    if len(word) >= int(size):
                        print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                        m_global_list.append(word) 
                
# Generate words mixed common_middle common_last
def set_333():
    a = permutations(data_list(),2)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                for g in common_last:
                    word = str(c).join(x)+str(g)
                    if len(word) >= int(size):
                        print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                        m_global_list.append(word)
    a = permutations(data_list(),3)
    for x in list(a):
        if not ''.join(x).isdigit():
            for c in common_middle:
                for g in common_last:
                    word = str(c).join(x)+str(g)
                    if len(word) >= int(size):
                        print("Progress: "+color.YELLOW+str(len(m_global_list))+color.END, end="\r")
                        m_global_list.append(word)