num = int(input("Insira um numero: "))
def verificar_par(num):
    if(num % 2 == 0):
        print("Esse numero é Par!!!")
    else:
        print("Esse numero é Impar!!!")
    return 0
print(verificar_par(num))        