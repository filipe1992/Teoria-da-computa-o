'''
Created on 30 de nov de 2018

@author: filiped
'''
class Base:
    def __init__(self):
        self.s=""
        self.p=0
        self.fim="@"
        
    def le_palavra(self,palavra="@"):
        self.p=0
        self.s = palavra+"@"
    
    def xp(self,c=""):
        return self.s[self.p]==c
    
    def np(self):
        self.p+=1
        return True
    
    def aceite(self):
        return "aceitou: "+str(self.p+1)
    
    def rejeicao(self):
        return "rejeitou: "+str(self.p+1)
