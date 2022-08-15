from time import sleep
number1 = float(input("Primeiro valor: "))
number2 = float(input("Segundo valor: "))
option = 0
while option != 6:
    print("Carregando menu...")
    sleep(1.5)
    print("""
[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
[5] ALTERAR VALORES
[6] ENCERRAR PROGRAMA
""")
    option = int(input("Escolha uma opção: "))
    if option == 1:
        result = number1 + number2
        print(f"A soma entre os valores {number1} e {number2} é igual a {result}")
    elif option == 2:
        result = number1 - number2
        print(f"A subtração entre os valores {number1} e {number2} é igual a {result}")
    elif option == 3:
        result = number1 * number2
        print(f"A multiplicação entre os valores {number1} e {number2} é igual a {result}")
    elif option == 4:
        result = number1 // number2
        print(f"A divisão entre os valores {number1} e {number2} é igual a {result}")
    elif option == 5:
        print("Informe os numeros novamente: ")
        number1 = float(input("Primeiro valor: "))
        number2 = float(input("Segundo valor: "))
    else:
        print("Finalizando o programa...")
    sleep(1.5)
print("Programa finalizado!")