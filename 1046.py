n = [int(i) for i in input().split()]
horas = []
for c in range(0,25):
    horas.append(c)
quant = 1
inicio = n[0]
fim = n[1]
contador = (horas.index(n[0])+1)
while True:
    if(contador >= 24):
        contador = 0
    if(horas[contador] == n[1]):
        break
    quant += 1
    contador += 1

print("O JOGO DUROU {} HORA(S)".format(quant))
