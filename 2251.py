c = 1
while True:
    n = int(input())
    if n == 0:
        break
    else:
        result = (2 **(n)) - 1
        print('Teste {}'.format(c))
        print('{}\n'.format(result))
        c += 1
        