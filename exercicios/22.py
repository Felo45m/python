from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual a sua jogada? "))
print("-="*13)
print(f"O comoutador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("-="*13)
if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador venceu!")
    elif jogador == 2:
        print("Computador venceu!")
    else:
        print("Jogada invalida!")
elif computador == 1:
    if jogador == 0:
        print("Computador venceu!")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador venceu!")
    else:
        print("Jogada invalida!")
elif computador == 2:
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador == 1:
        print("Computador venceu!")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Jogada invalida!")