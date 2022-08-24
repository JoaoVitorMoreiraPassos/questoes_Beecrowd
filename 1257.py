valores = { 'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,
            'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,
            'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,
            'Z':25}
n = int(input())
for c in range(n):
    quant_linhas = int(input())
    val_hash = 0
    for i in range(quant_linhas):
        letras = str(input())
        letras = list(letras)
        for j in range(len(letras)):
            val_hash += valores[letras[j]] + i + j
    print(val_hash)