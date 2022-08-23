while True:
    num = int(input("Digite um numero para ver sua tabuada de multiplicação: "))
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {num*c}")
print('tabuada encerrada')