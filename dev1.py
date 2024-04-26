def cria_mapa(n):
    l = []
    l2 = []
    for x in range(n):
        l2.append(' ')
    for x in range(n):
        l.append(l2)
    return l

def printa_string(l):
    print("COMPUTADOR - Austrália                   JOGADOR - Austrália")
    print("    A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ")
