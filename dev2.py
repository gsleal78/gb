from random import randint
from random import choice
import time
d={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
def string(l):
    string=''
    for i in l:
        for k in i:
            string +=k
        string+='\n'
    return string
def cria_mapa(n):
    l = []
    for _ in range(n):
        l2 = []
        for _ in range(n):
            l2.append(' ')
        l.append(l2)
    return l
def posicao_suporta(m,n,l,c,o):
    if o=='h':
        if c+n>len(m[0]):
            return False
        for i in range(n):
            if m[l][i+c]=='N':
                return False
        return True
    elif o=='v':
        if l+n>len(m):
            return False
        for i in range(n):
            if m[l+i][c]=='N':
                return False
        return True
def aloca_navios(m, l):
    for i in l:
        while True:
            linha = randint(0, len(m) - 1)
            coluna = randint(0, len(m[0]) - 1)
            orientacao = choice(['h', 'v'])
            if posicao_suporta(m, i, linha, coluna, orientacao):
                break
        if orientacao == 'h':
            for a in range(i):
                m[linha][a + coluna] = 'N'
        else:
            for a in range(i):
                m[linha + a][coluna] = 'N'
    return m
def foi_derrotado(l):
    for i in range(len(l)):
        for k in range(len(l[i])):
            if l[i][k]=='N':return False
    return True
mapa = cria_mapa(10)

