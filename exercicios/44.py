number = cont =soma = 0
while True:
    number = int(input("Digite um numero [999 para parar]: "))
    if number == 999:
        break
    soma += number
    cont += 1
print(f"A soma entre os {cont} valores é igual a {soma}")