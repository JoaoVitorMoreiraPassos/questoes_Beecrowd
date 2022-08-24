C = int(input())
while C>0:
    os = (input().split(' '))
    N = int(os[0])
    M = int(os[1])
    if (N) % (M) == 0:
        q = (N) / (M)
    elif (N) % (M) != 0:
        q = (N // M) + 1
    print('%d'%q)
    C -= 1
    