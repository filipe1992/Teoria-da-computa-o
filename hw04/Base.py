'''
Created on 30 de nov de 2018

@author: filiped
'''
class Base:
    def __init__(self):
        self.s=""
        self.p=0
        self.fim="@"
        
        self.pilha = ["z0"]
        
    def le_palavra(self,palavra="@"):
        self.p=0
        self.s = palavra+"@"
    
    def xp(self,c=""):
        print(self.s[self.p]==c, self.s[self.p], c)
        return self.s[self.p]==c
    
    def np(self):
        self.p+=1
        return True
    
    def aceite(self):
        return "aceitou: "+str(self.p+1)
    
    def rejeicao(self):
        return "rejeitou: "+str(self.p+1)
#------------------------------------------------------------------------------ 
    def topo(self,val):
        if val == self.pilha[-1]:
            self.pop()
            return True
        return False
    
    def put(self,val):
        print(self.pilha)
        self.pilha.append(val)
        return True
    
    def pop(self):
        print(self.pilha)
        return self.pilha.pop(-1)
    
    def esta_vazia(self):
        print(self.pilha)
        return len(self.pilha) > 0
#------------------------------------------------------------------------------ 

    def verificar(self, func):
        if func and self.xp(self.fim):
            print(self.aceite())
        else:
            print(self.rejeicao())
#------------------------------------------------------------------------------ 
    def w(self,val):
        print(val)
        return True
            
    
    
