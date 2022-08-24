a = []
for c in range(10):
    a.append(int(input()))
    if(a[c] <= 0):
        a[c] = 1
for c in range(0,10):
    print("X[{}] = {}".format(c,a[c]))