from time import sleep


num1 = int(input("Digite um numero: "))

def contagem_regressiva(i):
    print("Contagem regressiva")
    for i in range(i,0,-1):
        print(i)
        sleep(1)
    return 0
print(contagem_regressiva(num1))