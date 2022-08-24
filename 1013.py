n = input().split(' ')
a = n[0]
b = n[1]
c = n[2]
maiorab=(int(a)+int(b)+abs(int(a)-int(b)))/2
res=(int(maiorab)+int(c)+abs(int(maiorab)-int(c)))/2
print('%d eh o maior'%res)