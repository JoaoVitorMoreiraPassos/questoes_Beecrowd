salario = float(input())
if 0 <= salario <= 400.00:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 15 %'''.format(salario+(salario*0.15),(salario+(salario*0.15))-salario))
elif 400.01 <= salario <= 800.00:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 12 %'''.format(salario+(salario*0.12),(salario+(salario*0.12))-salario)) 
elif 800.01 <= salario <= 1200.00:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 10 %'''.format(salario+(salario*0.10),(salario+(salario*0.10))-salario))
elif 1200.01 <= salario <= 2000.00:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 7 %'''.format(salario+(salario*0.07),(salario+(salario*0.07))-salario))
else:
    print('''Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 4 %'''.format(salario+(salario*0.04),(salario+(salario*0.04))-salario))
