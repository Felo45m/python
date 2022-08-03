#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver 
#o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.



salario = float(input("Informe o seu salario: R$"))
a1 = "20%"
a2 = "15%"
a3 = "10%"
a4 = "5%"
if salario < 280:
    novoSalario = salario + (salario * 20/100)
    print(f"O salario de R${salario} terá uma aumento de {a1} e ficará R${novoSalario}")
elif (salario >= 280) and (salario < 700):
    novoSalario = salario + (salario * 15/100)
    print(f"O salario de R${salario} terá uma aumento de {a2} e ficará R${novoSalario}")
elif (salario >= 700) and (salario < 1500):
    novoSalario = salario + (salario * 10/100)
    print(f"O salario de R${salario} terá uma aumento de {a3} e ficará R${novoSalario}")
elif salario > 1500:
    novoSalario = salario + (salario * 5/100)
    print(f"O salario de R${salario} terá uma aumento de {a4} e ficará R${novoSalario}")