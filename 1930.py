def tira(n):
    return n -1
n = [int(i) for i in input().split()]
n = list(map(tira, n))
n[3] += 1
print(sum(n))