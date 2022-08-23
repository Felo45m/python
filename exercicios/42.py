resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    number = int(input("Digite um numero: "))
    soma += number
    quant += 1
    if quant == 1:
        maior = menor = number
    else:
        if number > maior:
            maior = number
        if number < menor:
            menor = number
    resp = str(input("Quer continuar? [S|N] ")).upper().strip()[0]
media = soma / quant
print(f"Você digitou {quant} numeros e a media entre eles foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
print("FIM DO PROGRAMA!")