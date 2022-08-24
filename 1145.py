x,y = [int(i) for i in input().split()]
a = 1
for c in range(0,y):
    if(a % x != 0):
        print(a, end=" ")
    else:
        print(a)
    a += 1
