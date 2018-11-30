'''
Created on 30 de nov de 2018

@author: filiped
'''
'''
Implemente em uma linguagem de programação de sua preferência
autômatos de pilha que reconheçam as linguagens:
    a) L = {a^n b^n c^m / n >= 0, m >= 1}
    b) L = {a^n b^(3n+1) / n >= 1}
'''

from hw04.Base import Base
b = Base()
#------------------------------------------------------------------------------ 

def mainA():
    b.le_palavra("aaabbbccc")
    def S(): return A() and C()
    def A(): return (b.xp("a") and b.np() and A() and b.xp("b") and b.np()) or True
    def C(): return (b.xp("c") and b.np() and Cl())
    def Cl():return (C() or True)
    b.verificar(S())
    
def main():
    b.le_palavra("aabbbbbb")
    

if __name__ == '__main__':
    main()