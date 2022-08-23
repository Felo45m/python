number = count = soma = 0
number = int(input("Digite um numero [999 para parar]: "))
while number != 999:
    soma += number
    count += 1
    number = int(input("Digite um numero [999 para parar]: "))
print(f"Você digitou {count} numeros e a soma entre eles é igual a {soma}")
