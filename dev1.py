def cria_mapa(n):
    l = []
    l2 = []
    for x in range(n):
        l2.append(' ')
    for x in range(n):
        l.append(l2)
    return l

print(cria_mapa(10))

def printa_string(l):
    string=''
    for i in l:
        for k in i:
            string +=k
        string+='\n'
    return string

espaco = cria_mapa(10)
espaco [0][0] = "gui"
print(printa_string(espaco))

print("""""
===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= 
Iniciando o Jogo!
Computador está alocando os navios de guerra do país Rússia...
Computador já está em posição de batalha!
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
""")
pergunta_inicial = input("Qual o número da nação da sua frota?")