from time import sleep
number1 = float(input("Primeiro valor: "))
number2 = float(input("Segundo valor: "))
option = 0
while option != 5:
    print("""
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
""")
    option = int(input("Escolha uma opção: "))
    if option == 1:
        result = number1 + number2
        print(f"A soma entre {number1} e {number2} é igual {result}.")
    elif option == 2:
        result = number1 * number2
        print(f"A multiplicação entre {number1} e {number2} é igual {result}.")
    elif option == 3:
        if number1 > number2:
            print(f"O número {number1} é maior que o numero {number2}.")
        elif number2 > number1:
            print(f"O número {number2} é maior que o numero {number1}.")
    elif option == 4:
        print("Informe os numeros novamente: ")
        number1 = float(input("Primeiro valor: "))
        number2 = float(input("Segundo valor: "))
    elif option == 5:
        print("Finalizando...")
        sleep(1)
    else:
        print("Opção invalida! Tente novamente.")
print("Fim do programa!")
