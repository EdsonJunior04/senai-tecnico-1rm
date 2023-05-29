n1 = float(input("Qual a primeira nota  ? "))
n2 = float(input("Qual a segunda nota  ? "))
n3 = float(input("Qual a terceira nota  ? "))


media = (n1 + n2 +n3)/3

print("A media do aluno é : {:.1f}".format(media))

if(media >= 50):
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
