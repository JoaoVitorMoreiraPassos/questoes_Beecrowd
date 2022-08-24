n = int(input())

for c in range(n):
    matriz= list()
    up = left = right = down = num_2048 = False
    for i in range(4):
        matriz.append([int(i) for i in input().split()])
    for i in range(4):
        for j in range(4):
            if i > 0:
                if matriz[i][j] != 0 and (matriz[i][j] == matriz[i-1][j] or matriz[i-1][j] == 0):
                    up = True
            if i < 3:
                if matriz[i][j] != 0 and (matriz[i][j] == matriz[i+1][j] or matriz[i+1][j] == 0):
                    down = True
            if j > 0:
                if matriz[i][j] != 0 and (matriz[i][j] == matriz[i][j-1] or matriz[i][j-1] == 0):
                    left = True
            if j < 3:
                if matriz[i][j] != 0 and (matriz[i][j] == matriz[i][j+1] or matriz[i][j+1] == 0):
                    right= True
            if matriz[i][j] == 2048:
                num_2048 = True
                up = False
                left = False
                down = False
                right = False
                break
        if num_2048 == True:
            break
    apresenta = []
    if(num_2048 == True or not(down or left  or right or up)):
        print('NONE')
    if(down):
        apresenta.append('DOWN')
    if(left):
        apresenta.append('LEFT')
    if(right):
        apresenta.append('RIGHT')
    if(up):
        apresenta.append('UP')
    for i in range(len(apresenta)):
        if i != len(apresenta) -1:
            print(apresenta[i],end=' ')
        elif i == len(apresenta) -1:
            print(apresenta[i])

