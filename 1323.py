N = int(input())
l = []
con = i = 0
while not(N == 0):
    l.append(N)
    N = int(input())
    con += 1
lc = list(map(lambda x:(x*(x+1)*(x*2 + 1))/6, l))
for c in range(0,con):
    print('%d'%lc[i])
    i += 1