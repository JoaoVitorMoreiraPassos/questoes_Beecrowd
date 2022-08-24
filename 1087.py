while True:
    cont = 0
    coordenadas = [int(i) for i in input().split()]
    if sum(coordenadas) == 0:
        break
    else:
        if coordenadas[0] == coordenadas[2] and coordenadas[1] == coordenadas[3]:
            print('0')
        elif((coordenadas[2]-coordenadas[0]) == -(coordenadas[3]-coordenadas[1]) or -(coordenadas[2]-coordenadas[0]) == -(coordenadas[3]-coordenadas[1]) or -(coordenadas[2]-coordenadas[0]) == (coordenadas[3]-coordenadas[1]) or (coordenadas[2]-coordenadas[0]) == (coordenadas[3]-coordenadas[1])):
            print('1')
        elif coordenadas[0] == coordenadas[2] or coordenadas[1] == coordenadas[3]:
            print('1')
        else:
            print('2')