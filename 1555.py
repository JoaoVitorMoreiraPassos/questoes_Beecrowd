N = int(input())
con = 0
reslist = []
while con < N:
    n = input().split(' ')
    x = int(n[0])
    y = int(n[1])
    r = (3*x)** 2 + y ** 2
    b = 2 * (x**2) + (5*y)**2
    c = (-100*x)+y**3
    mrrb = (r +b +abs(r-b))/2
    res = (mrrb + c + abs(mrrb - c))/2
    if res == r:
        reslist.append('Rafael ganhou')
    elif res == b:
        reslist.append('Beto ganhou')
    elif res == c:
        reslist.append('Carlos ganhou')
    con += 1
j = 0    
for c in range(0, N):
    print(reslist[j])
    j += 1