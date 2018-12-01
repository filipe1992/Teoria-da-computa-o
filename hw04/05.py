'''
Created on 30 de nov de 2018

@author: filiped
'''
'''
Implemente em linguagem de programação à sua escolha o algoritmo
CYK. Seu programa deve receber como entrada uma gramática livre de
contexto na Forma Normal de Chomsky e uma string de teste da
gramática. Descreva como deverá ser o formato dessa gramática.
'''
g = {"AA": ["S"],
     "AS": ["S","A"],
     "b": ["S"],
     "SA": ["A"],
     "a": ["A"]
    }

c = "abaab" 

def produzido_por(val):
    if val in g:
        return g[val]
    return []

def printmat(mat):
    for i in mat[::-1]:
        print(i)

def passo1(mat,cadeia):
    mat[1]= [g[i] for i in cadeia]

def roldana(mat, n):
    for s in range(2,n+1):
        for r in range(n-s+1):
            mat[s][r]=[]     
            for k in range(1,s):
                for i in mat[k][r]:
                    for j in mat[s-k][r+k]:
                        aux = produzido_por(i+j)
                        for a in aux:
                            if not (a in mat[s][r]): 
                                mat[s][r]+= a 
                            

def CYK(gramatica, cadeia):
    mat = [list(cadeia)]+[[""]*len(cadeia) for _ in range(len(cadeia))]
    passo1(mat,cadeia)
    print("\n#------------------------------Primeiro Passo-------------------------------------\n\n")
    printmat(mat)
    roldana(mat, len(cadeia))
    print("\n#------------------------------Completo-------------------------------------\n\n")
    printmat(mat)

CYK(g, c)

    
