num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if num1 > num2:
    print(f'{num1} é o maior numero')
elif num2 > num1:
    print(f"{num2} é o maior numero")
elif num1 == num2:
    print(f"os numeros {num1} e {num2} são iguais")
