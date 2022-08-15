from random import randint
computer = randint(0, 10)
print("""Acabei de pensar em um numero entre 0 e 10.
Você consegue adivinhar qual foi? """)
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpites += 1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print("Mais... Tente mais uma vez.")
        elif jogador > computer:
            print("Menos... Tente mais uma vez")
print(f"Acertou com {palpites} palpites.")