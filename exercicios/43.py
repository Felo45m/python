print("=-"*10)
print("VALIDADOR DE DADOS")
print("=-"*10)
name = str(input("Digite seu nome [Acima de 3 caracteres]: "))
age = int(input("Digite sua idade [Entre 0 e 150 ano]: "))
salario = float(input("Digite seu salario [Maior que 0]: "))
sexo = str(input("DIgite seu sexo [f/m]: ")).upper().strip()[0]
EstCivil = str(input("Digite seu estado civil [s, c, v, d]: ")).upper().strip()[0]

while True:
    tamanho = len(name)
    if tamanho > 3:
        True
    else:
        name = str(input("Nome invalido, digite novamente [Acima de 3 caracteres]: "))
    if age >= 0 or age <= 150:
        True
    else:
        age = int(input("Idade invalida, digite novamente [Entre 0 e 150 ano]: "))
    if salario > 0:
        True
    else:
        salario = float(input("Salario invalido, digite novamente [Maior que 0]: "))
        while sexo not in 'MmFf':
            sexo = str(input("Sexo invalido, digite novamente [f/m]: ")).strip().upper()[0]
        while EstCivil not in 'SsCcVvDd':
            EstCivil = str(input("Estado civil invalido, digite novamente [s, c, v, d]: ")).strip().upper()[0]
    break
print("Validação ok")