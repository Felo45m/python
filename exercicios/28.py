prim = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = prim + (10 - 1) * razao
for c in range(prim, decimo + razao, razao):
    print(f"{c}", end=" - ")
print("Fim!")
