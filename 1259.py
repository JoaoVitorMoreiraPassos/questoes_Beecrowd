n = int(input())

numeros = list()
for c in range(n):
    numeros.append(int(input()))
par = list()
impar = list()
for c in range(n):
    if numeros[c] % 2 == 0:
        par.append(numeros[c])
    else:
        impar.append(numeros[c])
numeros.clear()
par.sort()
impar.sort(reverse=True)
for c in range(0,len(par)):
    print(par[c])
for c in range(0,len(impar)):
    print(impar[c])
