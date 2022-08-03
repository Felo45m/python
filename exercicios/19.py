n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite outro numero: '))

if n1 > n2 and n3:
    print(f'{n1} é o maior numero.')
elif n2 > n1 and n3:
    print(f'{n2} é o maior numero.')
elif n3 > n2 and n1:
    print(f'{n3} é o maior numero.')
elif n1 == n2 == n3:
    print('Os numeros são iguais') 
    