from random import randint
v = 0
while True:
    jogador = int(input("Digite um valor: "))
    computer = randint (0,11)
    total = jogador + computer
    type = " "
    while type not in "PpIi":
        type = str(input("Par ou impar")).strip().upper()[0]
    print(f"voce jogo {jogador} e o computador {computer}. Total de {total}")
    if type == "P":
        if total % 2 == 0:
            print("Você Venceu!")
            v += 1
        else:
            print("Você perdeu!")
            break
    elif type == "I":
        if total % 2 == 0:
            print("Você venceu")
            v += 1
        else:
            print("Você perdeu!")
            break
        print("Novamente...")
print("Jogo encerrado!")