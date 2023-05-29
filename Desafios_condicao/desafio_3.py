salario = float(input("Digite um valor: "))

if salario > 8250:
    reajuste = salario * 10/100
    print("Reajuste ", salario + reajuste)
else:
    reajuste = salario * 15/100
    print("Reajuste ", salario + reajuste)
