n = input().split(' ')
lista = []
for c in range(0,4):
    lista.append(int(n[c]))
if lista[0] * lista[1] == lista[2] * lista[3]:
    print('0')
elif lista[0] * lista[1] > lista[2] * lista[3]:
    print('-1')
else:
    print('1')