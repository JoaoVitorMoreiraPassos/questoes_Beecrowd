L = int(input())
C = int(input())
l1 = (L * C) + (C-1)*(L-1)
l2 = 2*(C -1) + 2*(L-1)
a = [l1,l2]
for c in range(0,2):
    print('%d' %a[c])