'''
Created on 30 de nov de 2018

@author: filiped
'''
s=""
p=0

def le_palavra(palavra="@"):
    global s,p
    p=0
    s = palavra+"@"

def xp(c=""):
    global p
    return s[p]==c

def np():
    global p
    p+=1
    return True
if __name__ == '__main__':
    fim = "@"
    le_palavra("b@")
    while(xp("a") and np()):pass
    if xp("b") and np():
        while(xp("b") and np()):pass
    if xp(fim):
        print("reconheceu ate: ", (p+1))
    else:
        print("erro na posição: ", (p+1))
        
        
        
        
        
        