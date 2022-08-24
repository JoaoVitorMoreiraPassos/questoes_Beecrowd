n = int(input())
for loop in range(n):
    linha = list(str(input()))
    tam = int(len(linha))
    linha_invertida = []
    for i in range(int(tam/2)-1,-1, -1):
        linha_invertida.append(linha[i])
    for i in range(tam-1, int(tam/2)-1, -1):
        linha_invertida.append(linha[i])
    print("".join(linha_invertida))