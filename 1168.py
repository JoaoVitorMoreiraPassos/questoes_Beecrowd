d = {"1":2,
     "2":5,
     "3":5,
     "4":4,
     "5":5,
     "6":6,
     "7":3,
     "8":7,
     "9":6,
     "0":6
    }
n = int(input())
for c in range(n):
    num = (input())
    num = list(num)
    soma = 0
    for i in num:
        soma += d[i]
    print(f"{soma} leds")
