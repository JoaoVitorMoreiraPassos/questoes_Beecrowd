tf = True
while tf:
    while True:
        nota1 = float(input())
        if 0 <= nota1 <=10:
            break
        else:
            print('nota invalida')
    while True:
        nota2 = float(input())
        if 0 <= nota2 <= 10:
            break
        else:
            print('nota invalida')
    print('media = {0:.2f}'.format((nota1 + nota2)/2))
    while True:
        print('novo calculo (1-sim 2-nao)')
        paraounao = int(input())
        if paraounao == 1:
            break
        elif paraounao == 2:
            tf = False
            break
