n = [int(i) for i in input().split()]

if(n[0] % n[1] == 0 or n[1] % n[0] == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")