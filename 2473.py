nj = input().split()
ns = input().split()
cont = 0
for c in range(0,6):
    if nj[c] in ns:
        cont += 1
if cont < 3:
    print('azar')
if cont == 3:
    print('terno')
if cont == 4:
    print('quadra')
if cont == 5:
    print('quina')
if cont == 6:
    print('sena')