a = [int(i) for i in input().split()]
# horas = []
# for c in range(0,25):
#     horas.append(c)
# inicio = a[0:2]
# fim = a[2:4]

# quant_horas = 1

# contador = horas.index(inicio[0]) + 1

# while True:
#     if(contador >= 24):
#         contador = 0
#     if(horas[contador] == fim[0]):
#         break

#     quant_horas += 1
#     contador += 1

# quant_minutos = 0
# contador = inicio[1]
# while True:
#     if(contador == fim[1]):
#         break
#     quant_minutos += 1
#     contador += 1
#     if(contador == 60):
#         contador = 0
#     print(f"{contador}",end=" - ")
# print(quant_horas,quant_minutos)
quant_horas = 0
quant_minutos = 0
i = a[0] + 1
j = a[1]
while i != a[2]:
    while j != a[3]:
        j += 1
        if(j == 60):
            j = 0
        
        quant_minutos += 1
        print(j,end=" - ")
    if(i == 24):
        i = 0
    i += 1
    quant_horas += 1
print(quant_horas,quant_minutos)



















