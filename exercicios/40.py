number = int(input("Quantos termos você quer mostrar? "))
term1 = 0
term2 = 1
print(f"{term1} - {term2}", end="")
count = 3
while count <= number:
    term3 = term1 + term2
    print(f" - {term3}", end="")
    count += 1
    term1 = term2
    term2 = term3
print("FIM!")