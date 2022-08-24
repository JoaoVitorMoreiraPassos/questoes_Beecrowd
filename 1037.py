n = float(input())

array = [0,25,50,75,100]
for c in range(0,4):
    if(n > array[c] and n < array[c+1]):
        print('({},{}]'.format(array[c],array[c+1]))
        break
    elif(n == array[c]):
        print("[{},{}]".format(array[c],array[c+1]))
        break
    elif(n == array[c+1]):
        print("({},{}]".format(array[c],array[c+1]))
        break