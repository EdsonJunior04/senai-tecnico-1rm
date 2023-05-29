
print("MENU")
print("1 - Somar")
print("2 - Multiplicar")
print("3 - Maior")
print("4 - Menor")
numEsc = int(input("Escolha um numero: "))

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

def somar(n1,n2):
    total = n1 + n2
    return 'O resultado da soma foi: {}'.format(total)

def multiplicar(n1,n2):
    total = n1 * n2
    return 'O resultado da multiplicação foi: {}'.format(total)
    
def maior_menor(n1,n2):
    if(n1 > n2):
        return 'O {} é maior que {}'.format(n1,n2)
    if(n2 > n1):
        return  'O {} é menor que {}'.format(n2,n1)



if(numEsc == 1):
    print(somar(num1, num2))
elif (numEsc == 2):
    print(multiplicar(num1, num2))
elif(numEsc == 3):
    print(maior_menor(num1, num2))
elif(numEsc == 4): 
    print(maior_menor(num1, num2))
else:
    print("Preste atenção, digite um numero de 1 á 4!!! Tente novamente mais tarde")
