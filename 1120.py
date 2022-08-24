while True:
    a,b = input().split()
    if(a == "0" and b == "0"):
        break
    b = list(b)
    c = 0
    while True:
        try:
            if(b[c] == a):
                b.remove(a)
                c -= 1
        except:
            break
        c += 1
    c = 0
    try:
        while b[c] == "0":
            b.remove("0")
    except:
        pass
    if (len(b) == 0):
        b = "0"
    b = "".join(b)
    print(b)