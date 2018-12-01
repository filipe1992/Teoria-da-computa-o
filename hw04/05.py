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
     "a": ["A"],
     "SS":[] 
    }
c = "abaab" 

def printmat(mat):
    for i in mat[::-1]:
        print(i)

def passo1(mat,cadeia):
    mat[1]= [g[i] for i in cadeia]

def roldana(mat, n):
    for s in range(2,n+1):
        for r in range(n-s+1):
            mat[s][r]=[] 
            printmat(mat)
            print("\n\n")    
            for k in range(1,s):
                for i in mat[k][r]:
                    for j in mat[s-k][r+k]:
                        aux = g[i+j]
                        for a in aux:
                            if not (a in mat[s][r]): 
                                mat[s][r]+= a 
                            

def CYK(gramatica, cadeia):
    mat = [list(cadeia)]+[[""]*len(cadeia) for _ in range(len(cadeia))]
    printmat(mat)
    passo1(mat,cadeia)
    printmat(mat)
    roldana(mat, len(cadeia))
    printmat(mat)

CYK(g, c)

    
