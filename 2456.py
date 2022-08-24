l = input().split(' ')
if int(l[0]) < int(l[1]) < int(l[2]) < int(l[3]) < int(l[4]):
    print('C')
elif int(l[0]) > int(l[1]) > int(l[2]) > int(l[3]) > int(l[4]):
    print('D')
else:
    print('N')