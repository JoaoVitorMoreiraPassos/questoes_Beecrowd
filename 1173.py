n = int(input())
a = []
for c in range(10):
    a.append(n)
    n *= 2
for c in range(10):
    print("N[{}] = {}".format(c,a[c]))
