a = [i for i in input().split()]

produtos = {
    '1': 4,
    '2': 4.5,
    '3': 5.0,
    '4': 2,
    '5': 1.5
}

print(f'Total: R$ {produtos[a[0]] * int(a[1]) :.2f}')