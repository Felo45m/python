from calendar import c


number = int(input("Digite um numero: "))
count = number
fact = 1
while count > 0:
    print(f"{count}", end="")
    print(" x " if count > 1 else " = ", end="")
    fact *= count
    count -= 1
print(f"{fact}")
