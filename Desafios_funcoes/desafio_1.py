lar = float(input("Qual a largura? "))
comp = float(input("Qual o comprimento? "))

def area(num1,num2):
    result = num1 * num2
    return result

print("O total é: {}m²".format( area(lar, comp)))