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
    coluna = coordenada[1]
    for k,v in d.items(): 
        if letra == k: 
            linha = v

def valida_coordenada(coordenada):
    if coordenada[0] in 'ABCDEFGHIJ' and int(coordenada[1]) in range(1,11): 
        return True 
    return False 


