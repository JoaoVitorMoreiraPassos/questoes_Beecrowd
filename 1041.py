coord = [float(f) for f in input().split()]

if(coord[0] == 0 and coord[1] == 0):
    print("Origem")
elif(coord[0] == 0 and coord[1] != 0):
    print("Eixo Y")
elif(coord[0] != 0 and coord[1] == 0):
    print("Eixo X")
elif(coord[0] >= 0 and coord[1] >= 0):
    print("Q1")
elif(coord[0] >= 0 and coord[1] <= 0):
    print("Q4")
elif(coord[0] <= 0 and coord[1] <= 0):
    print("Q3")
elif(coord[0] <= 0 and coord[1] >= 0):
    print("Q2") 