p = str(input())
lista = list(p)
cont = 0
for c in lista:
    if c == 'p' and lista[cont+1] != 'p':
        del(lista[cont])
    if c == lista[-1]:
        break
    cont += 1
cont = 0    
for c in lista:
    if c == 'p' and lista[cont+1] in 'Pp':
        del(lista[cont])
    cont += 1
a = ''
for c in (lista):
    a += c
print(a)