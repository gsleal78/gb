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


DICIONARIO_CORES = {
    "A": '\u001b[34m▓▓▓\u001b[0m',
    "X": '\u001b[31m▓▓▓\u001b[0m',
    "V": '\u001b[32m▓▓▓\u001b[0m'
}

d={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}

def muda_cor(posicao): 
    if posicao == "N": 
        return "V"
    
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

def aloca_navios_jo(m, n,linha,coluna,orientacao):      
    if orientacao == 'h':
        for n2 in range(n):
            m[linha][n2 + coluna] = 'N'
    else:
        for n2 in range(n):
            m[linha + n2][coluna] = 'N'
    return m

def printa_string(l1,l2):
    for i in range(len(l2)): 
        for l in range(len(l2[i])): 
            if l2[i][l] == "N": 
                cor = "V"
                l2[i][l] = DICIONARIO_CORES[cor]
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
