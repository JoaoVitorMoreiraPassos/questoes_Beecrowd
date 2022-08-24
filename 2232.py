T = int(input())
cont = 0
j = 1
lista = []
while cont < T:
    N = int(input())
    r = 1
    for c in range(1,N):
            r = r +2**j
            j += 1
    lista.append(r)
    r = 1
    j = 1
    cont += 1
for c in range(0,T):
    print('%d' %lista[c])