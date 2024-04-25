def cria_mapa(n):
    l = []
    l2 = []
    for x in range(n):
        l2.append(' ')
    for x in range(n):
        l.append(l2)
    return l

print(cria_mapa(10))

def printa_string(listacomp):
    stringtotal = "   A   B   C   D   E   F   G   H   I    J  "*2
    string = ""
    leng = len(listacomp[0])
    for l in listacomp: 
        for i in range(leng):
            string+=  l[i]
        if stringtotal == "": 
            stringtotal+= string
        else: 
            stringtotal+="\n"+string
    return stringtotal
print(printa_string(cria_mapa(10)))


print("COMPUTADOR - Austrália                   JOGADOR - Brasil\n  A  B  C  D  E  F  G  H  I  J         A  B  C  D  E  F  G  H  I  J  \n1                                1    1                                1\n2                                2    2                                2")
'''    
  1                                1    1                                1
  2                                2    2                                2
  3                                3    3                                3
  4                                4    4                                4
  5                                5    5                                5
  6                                6    6                                6
  7                                7    7                                7
  8                                8    8                                8
  9                                9    9                                9
 10                                10  10                                10
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J 
'''