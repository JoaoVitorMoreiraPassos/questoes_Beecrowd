def converte(n):
    if(n.isnumeric()):
	    n = int(n)
    return n


n = int(input())
for c in range(n):
    nums = [str(n) for n in input().split()]
    nums = list(map( converte, nums))
    a = nums[0]
    b = nums[2]
    operador = nums[3]
    c = nums[4]
    d = nums[6]
    result = [0,0,0,0]
    if(operador == "+"):
        result[0] = a*d+c*b
        result[1] = b*d
    elif( operador == "-"):
        result[0] = a*d - c*b
        result[1] =  b*d
    elif( operador == "*"):
        result[0] = a*c
        result[1] = b*d
    elif(operador == "/"):
        result[0] = a*d
        result[1] = c*b
    menor = 1
    if(result[0] < result[1]):
        if(result[0] < 0):
            menor = result[0] * -1
        else:
            menor = result[0]
    elif(result[1] < result[0]):
        if(result[1] < 0):
            menor = result[1] * -1
        else:
            menor = result[1]
    else:
        result[2] = 1
        result[3] = 1
        print(f"{result[0]}/{result[1]} = {result[2]}/{result[3]}")
        continue
    mdc = 1
    for c in range(1,menor+1):
        if((result[0] % c == 0) and (result[1] % c) == 0):
            mdc = c
    if menor == 0:
        mdc = max(result[0],result[1])
    result[2] = (int(result[0] / mdc))
    result[3] = (int(result[1] / mdc))

    print(f"{result[0]}/{result[1]} = {result[2]}/{result[3]}")