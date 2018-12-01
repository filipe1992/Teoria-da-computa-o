'''
Created on 30 de nov de 2018

@author: filiped
'''

'''
 Implemente em linguagem de programação à sua escolha um
transdutor finito que, dada uma sequência de moedas de 25 e 50
centavos e de 1 real, forneça uma lata de refrigerante quando a
sequência totalizar 1 real ou mais. Cada moeda inserida deverá
corresponder a uma de duas saídas: 0, se uma lata não pode ser (ainda)
liberada, ou 1, se uma lata deve ser liberada. Um exemplo de entrada e
saída correspondente:
Entrada: 50 25 50 100 25 50 25 ....
Saída:   0  0  1   1  0  1  0  ...
'''
from hw04.Base import Base
b = Base()
#------------------------------------------------------------------------------ 

v = {"25": "0",
     "50": "1",
     "100": "2"
    }


def main():
    b.le_palavra("".join(v[i] for i in ["50", "25", "50", "100", "25", "50", "25"]))
    def S(): return (b.xp("2") and b.np() and b.w("1") and S()) or (b.xp("1") and b.np() and b.w("0") and A()) or (b.xp("0") and b.np() and b.w("0") and B())
    def A(): return (b.xp("2") and b.np() and b.w("1") and A()) or (b.xp("1") and b.np() and b.w("1") and S()) or (b.xp("0") and b.np() and b.w("0") and C())
    def B(): return (b.xp("2") and b.np() and b.w("1") and B()) or (b.xp("1") and b.np() and b.w("0") and C()) or (b.xp("0") and b.np() and b.w("0") and A())
    def C(): return (b.xp("2") and b.np() and b.w("1") and C()) or (b.xp("1") and b.np() and b.w("1") and B()) or (b.xp("0") and b.np() and b.w("1") and S())
    S()
    
if __name__ == '__main__':
    main()    
    
    
    