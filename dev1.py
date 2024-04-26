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
    "X": '\u001b[31m▓▓▓\u001b[0m'
}

d={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}

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

def aloca_navios_jo(m, l,linha,coluna,orientacao):
    for i in l:
        if posicao_suporta(m, i, linha, coluna, orientacao):       
            if orientacao == 'h':
                for a in range(i):
                    m[linha][a + coluna] = 'N'
            else:
                for a in range(i):
                    m[linha + a][coluna] = 'N'
        else: 
            return False
    return m


