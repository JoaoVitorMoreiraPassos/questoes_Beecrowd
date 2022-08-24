notas = [float(i) for i in input().split()]
pesos = [2,3,4,1]
for c in range(4):
    notas[c] *= pesos[c]
media = (sum(notas))/sum(pesos)
print("Media: {:.1f}".format(media))
if(media >= 7):
    print("Aluno aprovado.")
else:
    if (media < 5):
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        nota_exame = float(input())
        print("Nota do exame: {:.1f}".format(nota_exame))
        nota_final = (nota_exame + media)/ 2
        if(nota_final >= 5):
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: {:.1f}".format(nota_final))
