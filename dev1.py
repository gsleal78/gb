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
i = 0 
for s in mi: 
    if i == 0: 
        print(s)
        i+=1 
    else: 
        time.sleep(2)        
        print(s)
escolhe_pais = input("Qual o número da nação da sua frota?")
print("Otima escolha")
time.sleep(1)
print("Iniciando jogo!")