first = int(input("Primeiro termo: "))
reason = int(input("Razão: "))
term = first
count = 1
total = 0
most = 10
while most != 0:
    total = total + most
    while count <= total:
        print(f"{term} - ", end="")
        term += reason
        count += 1
    print("Pausa")
    most = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados!")