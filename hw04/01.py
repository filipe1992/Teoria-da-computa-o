'''
Created on 30 de nov de 2018

@author: filiped
'''
Q = '''
1. Implemente em uma linguagem de programação à sua escolha AFDs
que aceitem as seguintes cadeias:
    a) Todas as cadeias em (0,1)* que representam cada “1” seguido
        imediatamente de dois “0”.
    
    b) Todas as cadeias em (a,b)* de modo que o último símbolo seja “b”
        e o número de símbolos “a” seja par.
'''
from hw04.Base import Base



def mainA():
    b = Base()
    b.le_palavra("00100100")
    def A(): return (b.xp("0") and b.np() and A()) or (b.xp("1") and b.np() and B())
    def B():return (b.xp("0") and b.np() and C())
    def C(): return (b.xp("0") and b.np() and A())
    
    if A() and b.xp(b.fim):
        print(b.aceite())
    else:
        print(b.rejeicao())
 
 
def mainB():
    b = Base()
    b.le_palavra("abbaaab")
    def P(): return (b.xp("a") and b.np() and I()) or (b.xp("b") and b.np() and PB())
    def I(): return (b.xp("a") and b.np() and P()) or (b.xp("b") and b.np() and IB())
    def PB():return (b.xp("b") and b.np() and PB()) or (b.xp("a") and b.np() and I()) or True
    def IB():return (b.xp("b") and b.np() and IB()) or (b.xp("a") and b.np() and P())
    
    if P() and b.xp(b.fim):
        print(b.aceite())
    else:
        print(b.rejeicao())
    

if __name__ == '__main__':
    mainA()
    mainB()
    