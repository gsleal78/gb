from random import randint
from random import choice
import time

#DEFINIÇÕES NECESSÁRIAS 

d={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

mensagem_inicial = """=======================================
|                                     |
|   Bem-vindo ao CAMPO DE GUERRA      |
|                                     |
=======================================,
Iniciando o Jogo!,
Computador está alocando os navios de guerra do país Rússia...,
Computador já está em posição de batalha!,
Suas opções:,
1: Brasil
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes
2: França
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado
3: Austrália
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro
4: Rússia
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino
5: Japão
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino
"""

mi = mensagem_inicial.split(",")

#FUNÇÕES QUE VAMOS UTILIZAR 

def string(l):
    string=''
    for i in l:
        for k in i:
            string +=k
        string+='\n'
    return string
def cria_mapa(n):
    l = []
    for a in range(n):
        l2 = []
        for b in range(n):
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
mapausu = cria_mapa(10)
mapacomp = cria_mapa(10)
