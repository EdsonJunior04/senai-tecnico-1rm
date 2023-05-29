num1 = int(input("Insira um numero: "))
num2 = int(input("Insira um numero: "))
num3 = int(input("Insira um numero: "))

def maior(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
         numeroMaior = num1
    else:
        if(num2 > num1 and num2 > num3):
         numeroMaior = num2
        else :
         numeroMaior = num3
    return print("O maior numero é: ", numeroMaior)
 
print(maior(num1, num2, num3))

        
        