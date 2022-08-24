quants = [int(i) for i in input().split()]
marcadas = [int(i) for i in input().split()]
compradas = {int(i) for i in input().split()}
cont = 0
for c in compradas:
    if(c in marcadas):
        cont += 1
print(len(marcadas) - cont)