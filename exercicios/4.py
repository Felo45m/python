# Faça um Programa que peça as 4 notas bimestrais e mostre a média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
soma = n1 + n2 + n3 + n4
media = soma / 4
print(f'A media final foi igual a {media:.2f}')
