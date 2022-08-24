T = int(input())
con = 0
case = 1
lista = []
result = []
while con < T:
    a = input().split(' ')
    for c in range (0,len(a)):
        lista.append(int(a[c]))
    lista.sort()
    me = len(a) // 2 + 1
    result.append(lista[me-1])
    lista = []
    con += 1
j = 0
for c in range(1,con+1):
    print('Case %d: %d' %(c,result[j]))
    j += 1