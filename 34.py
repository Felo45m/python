n = int(input("Digite uma nota entre 0 e 10: "))
while n not in range(0, 11):
    n = int(input("Valor invalido! Digite uma nota valida: "))
print(f"Valor {n} validado!")
