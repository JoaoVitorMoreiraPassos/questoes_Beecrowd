n = [float(f) for f in input().split()]

n.sort(reverse=True)

if(n[2] + n[1] > n[0]):
    print("Perimetro = {}".format(sum(n)))
else:
    print("Area = {}".format(((n[0] + n[1])*n[2])/2))