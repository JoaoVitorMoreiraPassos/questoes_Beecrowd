while True:    
    n = int(input())
    if n == 0:
        break
    vetor = [int(i) for i in input().split()]

    mais_caro = mais_barato = vetor[0] + vetor[-1]
    vetor.pop()
    vetor.pop(0)
    x = int(len(vetor) / 2)
    cont = 0
    if len(vetor) > 0:
        for c in range(0, x):
            if (vetor[cont] + vetor[-1]) >= mais_caro:
                mais_caro = vetor[cont] + vetor[-1]
            elif vetor[cont] + vetor[-1] <= mais_barato:
                mais_barato = vetor[cont] + vetor[-1]
            vetor.pop()
            vetor.pop(0)
    print('{} {}'.format(mais_caro,mais_barato))