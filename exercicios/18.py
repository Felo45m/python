n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input("Digite a segunda nota do aluno: "))
media = (n1 + n2) / 2

if 7 <= media <= 9.99:
    print("Aluno APROVADO!")
elif media < 7:
    print("Aluno REPROVADO!")
elif media == 10:
    print("Aluno APROVADO COM DISTINÇÃO!!")
    