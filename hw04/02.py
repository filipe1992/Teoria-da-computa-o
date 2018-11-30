'''
Created on 30 de nov de 2018

@author: filiped
'''

'''
2. Implemente em uma linguagem de programação à sua escolha a
Gramática:
G=(V, T, P, S), onde:
V={W, A, B}
T={a,b}
P={
W-->AB
A --> aaaA | aaA | aA| a <=> A --> aA | a
B --> bB | []
}
'''


from hw04.Base import Base
b = Base()
#------------------------------------------------------------------------------ 

def main():
    global b
    b.le_palavra("a")
    def W(): return A() and B()
    def A(): return (b.xp("a") and b.np() and A()) or (b.xp("a") and b.np())
    def B(): return (b.xp("b") and b.np() and B()) or True
    
    if W() and b.xp(b.fim):
        print(b.aceite())
    else:
        print(b.rejeicao())


if __name__ == '__main__':
    main()
