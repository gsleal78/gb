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
