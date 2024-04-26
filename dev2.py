from random import randint
from random import choice
import time

#DEFINIÇÕES NECESSÁRIAS 
listanumeros=['1','2','3','4','5']
d={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}
numeroparapais={1:'Brasil', 2:'França', 3:'Austrália', 4:'Rússia', 5:'Japão'}
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
Paises = ["Brasil","França","Austrália","Rússia","Japão"]
comp_pais = choice(Paises)

mensagem_inicial = f"""=======================================
|                                     |
|   Bem-vindo ao CAMPO DE GUERRA      |
|                                     |
=======================================,
Iniciando o Jogo!,
Computador está alocando os navios de guerra do país {comp_pais}...,
Computador já está em posição de batalha!,
Suas opções:,
1: Brasil
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes,
2: França
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado,
3: Austrália
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro,
4: Rússia
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino,
5: Japão
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino  
"""

mi = mensagem_inicial.split(",")
#FUNÇÕES QUE VAMOS UTILIZAR 

def printa_string(l1,l2):
    print("        COMPUTADOR - Austrália                                        JOGADOR - Austrália")
    print("    A  B  C  D  E  F  G  H  I  J                                 A  B  C  D  E  F  G  H  I  J ")
    print(f'  1{l1[0][0]}{l1[0][1]}{l1[0][2]}{l1[0][3]}{l1[0][4]}{l1[0][5]}{l1[0][6]}{l1[0][7]}{l1[0][8]}{l1[0][9]}1                             1{l2[0][0]}{l2[0][1]}{l2[0][2]}{l2[0][3]}{l2[0][4]}{l2[0][5]}{l2[0][6]}{l2[0][7]}{l2[0][8]}{l2[0][9]}1')
    print(f'  2{l1[1][0]}{l1[1][1]}{l1[1][2]}{l1[1][3]}{l1[1][4]}{l1[1][5]}{l1[1][6]}{l1[1][7]}{l1[1][8]}{l1[1][9]}2                             2{l2[1][0]}{l2[1][1]}{l2[1][2]}{l2[1][3]}{l2[1][4]}{l2[1][5]}{l2[1][6]}{l2[1][7]}{l2[1][8]}{l2[1][9]}2')
    print(f'  3{l1[2][0]}{l1[2][1]}{l1[2][2]}{l1[2][3]}{l1[2][4]}{l1[2][5]}{l1[2][6]}{l1[2][7]}{l1[2][8]}{l1[2][9]}3                             3{l2[2][0]}{l2[2][1]}{l2[2][2]}{l2[2][3]}{l2[2][4]}{l2[2][5]}{l2[2][6]}{l2[2][7]}{l2[2][8]}{l2[2][9]}3')
    print(f'  4{l1[3][0]}{l1[3][1]}{l1[3][2]}{l1[3][3]}{l1[3][4]}{l1[3][5]}{l1[3][6]}{l1[3][7]}{l1[3][8]}{l1[3][9]}4                             4{l2[3][0]}{l2[3][1]}{l2[3][2]}{l2[3][3]}{l2[3][4]}{l2[3][5]}{l2[3][6]}{l2[3][7]}{l2[3][8]}{l2[3][9]}4')
    print(f'  5{l1[4][0]}{l1[4][1]}{l1[4][2]}{l1[4][3]}{l1[4][4]}{l1[4][5]}{l1[4][6]}{l1[4][7]}{l1[4][8]}{l1[4][9]}5                             5{l2[4][0]}{l2[4][1]}{l2[4][2]}{l2[4][3]}{l2[4][4]}{l2[4][5]}{l2[4][6]}{l2[4][7]}{l2[4][8]}{l2[4][9]}5')
    print(f'  6{l1[5][0]}{l1[5][1]}{l1[5][2]}{l1[5][3]}{l1[5][4]}{l1[5][5]}{l1[5][6]}{l1[5][7]}{l1[5][8]}{l1[5][9]}6                             6{l2[5][0]}{l2[5][1]}{l2[5][2]}{l2[5][3]}{l2[5][4]}{l2[5][5]}{l2[5][6]}{l2[5][7]}{l2[5][8]}{l2[5][9]}6')
    print(f'  7{l1[6][0]}{l1[6][1]}{l1[6][2]}{l1[6][3]}{l1[6][4]}{l1[6][5]}{l1[6][6]}{l1[6][7]}{l1[6][8]}{l1[6][9]}7                             7{l2[6][0]}{l2[6][1]}{l2[6][2]}{l2[6][3]}{l2[6][4]}{l2[6][5]}{l2[6][6]}{l2[6][7]}{l2[6][8]}{l2[6][9]}7')
    print(f'  8{l1[7][0]}{l1[7][1]}{l1[7][2]}{l1[7][3]}{l1[7][4]}{l1[7][5]}{l1[7][6]}{l1[7][7]}{l1[7][8]}{l1[7][9]}8                             8{l2[7][0]}{l2[7][1]}{l2[7][2]}{l2[7][3]}{l2[7][4]}{l2[7][5]}{l2[7][6]}{l2[7][7]}{l2[7][8]}{l2[7][9]}8')
    print(f'  9{l1[8][0]}{l1[8][1]}{l1[8][2]}{l1[8][3]}{l1[8][4]}{l1[8][5]}{l1[8][6]}{l1[8][7]}{l1[8][8]}{l1[8][9]}9                             9{l2[8][0]}{l2[8][1]}{l2[8][2]}{l2[8][3]}{l2[8][4]}{l2[8][5]}{l2[8][6]}{l2[8][7]}{l2[8][8]}{l2[8][9]}9')
    print(f' 10{l1[9][0]}{l1[9][1]}{l1[9][2]}{l1[9][3]}{l1[9][4]}{l1[9][5]}{l1[9][6]}{l1[9][7]}{l1[9][8]}{l1[9][9]}10                           10{l2[9][0]}{l2[9][1]}{l2[9][2]}{l2[9][3]}{l2[9][4]}{l2[9][5]}{l2[9][6]}{l2[9][7]}{l2[9][8]}{l2[9][9]}10')            
    print("    A  B  C  D  E  F  G  H  I  J                                 A  B  C  D  E  F  G  H  I  J ")
    return ''

def aloca_navios_jo(m, n,linha,coluna,orientacao):      
    if orientacao == 'h':
        for n2 in range(n):
            m[linha][n2 + coluna] = 'N'
    else:
        for n2 in range(n):
            m[linha + n2][coluna] = 'N'
    return m

def verifica_stb(posicao):
    if posicao == "N": 
        return "X"
    else: 
        return "A"
    
def converte_coordenada(coordenada):
    letra = coordenada[0].lower()
    coluna = int(coordenada[1])-1
    for k,v in d.items(): 
        if letra == k: 
            linha = v
    coordenada2 = [linha,coluna]
    return coordenada2

def valida_coordenada(coordenada):
    if coordenada[0] in 'ABCDEFGHIJ' and int(coordenada[1]) in range(1,11): 
        return True 
    return False 

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
            l2.append('   ')
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


#JOGO EM SI 
i = 0 
for s in mi: 
    if i == 0: 
        print(s)
        i+=1 
    else: 
        time.sleep(0)        
        print(s)
mapausu = cria_mapa(10)
mapacomp = cria_mapa(10)
blocoscomp=[]
for a,b in PAISES[comp_pais].items():
    for i in range(b):
        blocoscomp.append(CONFIGURACAO[a])
mapacomp=aloca_navios(mapacomp,blocoscomp)
        
while True:
    frota = input("Qual o número da nação da sua frota?")
    if frota in listanumeros:
        break
    else:
        print("Opção inválida")
frota=int(frota)
print(f"Você escolheu a nação {numeroparapais[frota]}\nAgora é sua vez de alocar seus navios de guerra!")
lista = cria_mapa(10)

naviosusuario=[]
for a,b in PAISES[numeroparapais[frota]].items():
    for k in range(b):
        naviosusuario.append(a)
naviosusuario2=naviosusuario
del naviosusuario2[0]
for i in naviosusuario:
    while True:
        print(f'alocar: {i} {CONFIGURACAO[i]} blocos')
        print(f'próximos: {naviosusuario2}')
        coordenada = input('Informe a coordenada ex:A1')
        direção = input('Informe a Orientação [v|h]')
        direção=direção.lower()
        if direção in 'vh':
            if valida_coordenada(coordenada):
                coordenada = converte_coordenada(coordenada)
                if posicao_suporta(mapausu, CONFIGURACAO[i], coordenada[0], coordenada[1], direção):
                    mapausu=aloca_navios_jo(mapausu, CONFIGURACAO[i], coordenada[0], coordenada[1],direção)
                    print(printa_string(lista, mapausu))
                    break
                else:   print('Opção inválida')
            else:   print('Opção inválida')
        else:   print('Opção inválida')
