user = str(input("Digite um nome de usuario: "))
password = str(input("Digite uma senha: "))
while password == user:
    password = str(input("A senha não pode ser igual ao seu usuario! Informe uma nova senha: "))
print("Usuario e senha validados com sucesso.")
